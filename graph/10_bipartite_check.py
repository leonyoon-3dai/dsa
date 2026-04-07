"""
Graph Algorithm Example 10: Bipartite Graph Check
이분 그래프 판별 - 그래프의 노드를 두 그룹으로 나눌 수 있는지 확인하는 알고리즘

Problem: 무방향 그래프가 이분 그래프(Bipartite Graph)인지 판별하라.
이분 그래프: 모든 간선이 서로 다른 그룹의 노드를 연결하도록 두 그룹으로 나눌 수 있는 그래프
(LeetCode 785)
"""

from collections import deque


def is_bipartite_bfs(graph: dict, num_nodes: int) -> tuple:
    # 각 노드의 색상: -1=미방문, 0=그룹A, 1=그룹B
    color = [-1] * num_nodes

    # 모든 노드에서 BFS 시작 (연결되지 않은 컴포넌트도 확인)
    for start in range(num_nodes):
        # 이미 색칠된 노드는 건너뜀
        if color[start] != -1:
            continue

        # 시작 노드를 그룹A(0)로 색칠
        color[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()

            # 인접 노드 탐색
            for neighbor in graph.get(node, []):
                if color[neighbor] == -1:
                    # 미방문 노드: 현재 노드와 반대 색으로 칠함
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # 인접한 두 노드가 같은 색 → 이분 그래프 아님
                    return False, []

    # 두 그룹으로 분리
    group_a = [i for i in range(num_nodes) if color[i] == 0]
    group_b = [i for i in range(num_nodes) if color[i] == 1]

    return True, (group_a, group_b)


def is_bipartite_dfs(graph: dict, num_nodes: int) -> tuple:
    # 각 노드의 색상
    color = [-1] * num_nodes

    def dfs(node: int, c: int) -> bool:
        # 현재 노드를 색칠
        color[node] = c

        # 인접 노드 탐색
        for neighbor in graph.get(node, []):
            if color[neighbor] == -1:
                # 미방문 노드: 반대 색으로 재귀 탐색
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                # 같은 색의 인접 노드 → 이분 그래프 아님
                return False

        return True

    # 모든 노드에서 DFS 시작
    for node in range(num_nodes):
        if color[node] == -1:
            if not dfs(node, 0):
                return False, []

    group_a = [i for i in range(num_nodes) if color[i] == 0]
    group_b = [i for i in range(num_nodes) if color[i] == 1]

    return True, (group_a, group_b)


# === 실행 예제 ===
if __name__ == "__main__":
    # 이분 그래프 (짝수 사이클)
    bipartite_graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }

    # 이분 그래프가 아닌 그래프 (홀수 사이클)
    non_bipartite_graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    print("=== Bipartite Graph Check (BFS) ===")
    is_bip, groups = is_bipartite_bfs(bipartite_graph, 4)
    print(f"정사각형 그래프: 이분 그래프 = {is_bip}")
    if is_bip:
        print(f"  그룹 A: {groups[0]}")
        print(f"  그룹 B: {groups[1]}")

    is_bip, groups = is_bipartite_bfs(non_bipartite_graph, 3)
    print(f"삼각형 그래프: 이분 그래프 = {is_bip}")

    print("\n=== Bipartite Graph Check (DFS) ===")
    # 더 큰 이분 그래프 예제
    larger_bipartite = {
        0: [3, 4],
        1: [3, 5],
        2: [4, 5],
        3: [0, 1],
        4: [0, 2],
        5: [1, 2]
    }

    is_bip, groups = is_bipartite_dfs(larger_bipartite, 6)
    print(f"6노드 이분 그래프: 이분 그래프 = {is_bip}")
    if is_bip:
        print(f"  그룹 A: {groups[0]}")
        print(f"  그룹 B: {groups[1]}")
