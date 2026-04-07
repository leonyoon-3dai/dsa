"""
Graph Algorithm Example 5: Topological Sort
위상 정렬 - DAG(방향 비순환 그래프)에서 노드를 선형으로 정렬하는 알고리즘

Problem: 방향 그래프에서 모든 간선 (u, v)에 대해 u가 v보다 먼저 오도록 정렬하라.
(선수과목 관계, 작업 순서 등에 활용)
"""

from collections import deque


def topological_sort_kahn(graph: dict, num_nodes: int) -> list:
    # 각 노드의 진입 차수(들어오는 간선 수)를 계산
    in_degree = [0] * num_nodes

    # 모든 간선을 확인하여 진입 차수 계산
    for node in range(num_nodes):
        for neighbor in graph.get(node, []):
            in_degree[neighbor] += 1

    # 진입 차수가 0인 노드를 큐에 넣음 (시작점들)
    queue = deque()
    for node in range(num_nodes):
        if in_degree[node] == 0:
            queue.append(node)

    # 정렬 결과를 저장할 리스트
    result = []

    # 큐가 빌 때까지 반복
    while queue:
        # 진입 차수가 0인 노드를 꺼냄
        node = queue.popleft()
        result.append(node)

        # 현재 노드에서 나가는 간선을 제거 (진입 차수 감소)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1

            # 진입 차수가 0이 되면 큐에 추가
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 모든 노드가 정렬되었는지 확인 (순환이 있으면 일부 누락됨)
    if len(result) != num_nodes:
        return []  # 순환이 존재하여 위상 정렬 불가능

    return result


def topological_sort_dfs(graph: dict, num_nodes: int) -> list:
    # 방문 상태: 0=미방문, 1=방문중, 2=완료
    state = [0] * num_nodes

    # 결과를 역순으로 저장할 리스트
    result = []

    # 순환 감지 플래그
    has_cycle = False

    def dfs(node: int):
        nonlocal has_cycle

        # 순환이 감지되면 즉시 종료
        if has_cycle:
            return

        # 현재 노드를 방문중으로 표시
        state[node] = 1

        # 인접 노드 탐색
        for neighbor in graph.get(node, []):
            if state[neighbor] == 1:
                # 방문중인 노드를 다시 만남 → 순환 존재
                has_cycle = True
                return
            if state[neighbor] == 0:
                # 미방문 노드 탐색
                dfs(neighbor)

        # 현재 노드의 탐색 완료
        state[node] = 2

        # 후위 순서로 결과에 추가 (나중에 뒤집어야 함)
        result.append(node)

    # 모든 노드에서 DFS 시작
    for node in range(num_nodes):
        if state[node] == 0:
            dfs(node)

    # 순환이 있으면 빈 리스트 반환
    if has_cycle:
        return []

    # 후위 순서를 뒤집어서 위상 정렬 결과를 만듦
    result.reverse()
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 선수과목 관계를 나타내는 방향 그래프
    # 0: 수학기초, 1: 미적분, 2: 선형대수, 3: 확률통계, 4: 머신러닝, 5: 딥러닝
    graph = {
        0: [1, 2],      # 수학기초 → 미적분, 선형대수
        1: [3, 4],      # 미적분 → 확률통계, 머신러닝
        2: [4],          # 선형대수 → 머신러닝
        3: [5],          # 확률통계 → 딥러닝
        4: [5],          # 머신러닝 → 딥러닝
        5: []            # 딥러닝
    }

    labels = {0: "수학기초", 1: "미적분", 2: "선형대수", 3: "확률통계", 4: "머신러닝", 5: "딥러닝"}

    print("=== Topological Sort (Kahn's Algorithm - BFS) ===")
    result_kahn = topological_sort_kahn(graph, 6)
    print(f"정렬 결과: {result_kahn}")
    print(f"과목 순서: {' → '.join(labels[n] for n in result_kahn)}")

    print("\n=== Topological Sort (DFS) ===")
    result_dfs = topological_sort_dfs(graph, 6)
    print(f"정렬 결과: {result_dfs}")
    print(f"과목 순서: {' → '.join(labels[n] for n in result_dfs)}")

    # 순환이 있는 그래프
    print("\n=== 순환이 있는 그래프 ===")
    cyclic_graph = {0: [1], 1: [2], 2: [0]}
    result = topological_sort_kahn(cyclic_graph, 3)
    print(f"결과: {result if result else '순환 존재 - 위상 정렬 불가능'}")
