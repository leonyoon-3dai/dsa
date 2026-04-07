"""
Graph Algorithm Example 6: Cycle Detection
순환 탐지 - 그래프에 순환(사이클)이 존재하는지 판별하는 알고리즘

Problem: 방향 그래프와 무방향 그래프에서 순환이 존재하는지 확인하라.
"""


def has_cycle_directed(graph: dict, num_nodes: int) -> bool:
    # 방문 상태: 0=미방문, 1=방문중(현재 경로), 2=완료
    state = [0] * num_nodes

    def dfs(node: int) -> bool:
        # 현재 노드를 방문중으로 표시
        state[node] = 1

        # 인접 노드 탐색
        for neighbor in graph.get(node, []):
            if state[neighbor] == 1:
                # 현재 경로에서 이미 방문한 노드를 만남 → 순환 존재
                return True
            if state[neighbor] == 0:
                # 미방문 노드를 재귀적으로 탐색
                if dfs(neighbor):
                    return True

        # 현재 노드의 탐색 완료
        state[node] = 2
        return False

    # 모든 노드에서 DFS 시작 (연결되지 않은 컴포넌트도 확인)
    for node in range(num_nodes):
        if state[node] == 0:
            if dfs(node):
                return True

    return False


def has_cycle_undirected(graph: dict, num_nodes: int) -> bool:
    # 방문 여부 기록
    visited = [False] * num_nodes

    def dfs(node: int, parent: int) -> bool:
        # 현재 노드를 방문 처리
        visited[node] = True

        # 인접 노드 탐색
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                # 미방문 노드를 재귀 탐색
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # 방문한 노드인데 부모가 아니면 → 순환 존재
                return True

        return False

    # 모든 노드에서 DFS 시작
    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node, -1):
                return True

    return False


def find_cycle_directed(graph: dict, num_nodes: int) -> list:
    # 순환을 찾아서 해당 경로를 반환
    state = [0] * num_nodes
    parent = [-1] * num_nodes

    def dfs(node: int) -> int:
        # 현재 노드를 방문중으로 표시
        state[node] = 1

        for neighbor in graph.get(node, []):
            if state[neighbor] == 1:
                # 순환 발견! 순환의 시작 노드를 반환
                parent[neighbor] = node
                return neighbor
            if state[neighbor] == 0:
                parent[neighbor] = node
                result = dfs(neighbor)
                if result != -1:
                    return result

        state[node] = 2
        return -1

    # 순환 탐지
    cycle_start = -1
    for node in range(num_nodes):
        if state[node] == 0:
            cycle_start = dfs(node)
            if cycle_start != -1:
                break

    # 순환이 없으면 빈 리스트 반환
    if cycle_start == -1:
        return []

    # 순환 경로 복원
    cycle = [cycle_start]
    current = parent[cycle_start]
    while current != cycle_start:
        cycle.append(current)
        current = parent[current]
    cycle.append(cycle_start)
    cycle.reverse()

    return cycle


# === 실행 예제 ===
if __name__ == "__main__":
    # 순환이 있는 방향 그래프
    directed_with_cycle = {
        0: [1],
        1: [2],
        2: [3],
        3: [1]  # 1 → 2 → 3 → 1 순환
    }

    # 순환이 없는 방향 그래프 (DAG)
    directed_no_cycle = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }

    print("=== Directed Graph Cycle Detection ===")
    print(f"순환 있는 그래프: {has_cycle_directed(directed_with_cycle, 4)}")
    print(f"순환 없는 그래프: {has_cycle_directed(directed_no_cycle, 4)}")

    print("\n=== Find Cycle Path ===")
    cycle = find_cycle_directed(directed_with_cycle, 4)
    print(f"순환 경로: {' → '.join(map(str, cycle))}")

    # 무방향 그래프
    undirected_with_cycle = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }

    undirected_no_cycle = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2]
    }

    print("\n=== Undirected Graph Cycle Detection ===")
    print(f"순환 있는 그래프: {has_cycle_undirected(undirected_with_cycle, 4)}")
    print(f"순환 없는 그래프: {has_cycle_undirected(undirected_no_cycle, 4)}")
