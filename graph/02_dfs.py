"""
Graph Algorithm Example 2: DFS (Depth-First Search)
깊이 우선 탐색 - 한 방향으로 깊이 들어가며 탐색하는 알고리즘

Problem: 그래프에서 시작 노드로부터 모든 노드를 깊이 우선으로 방문하라.
재귀 방식과 스택 방식 두 가지로 구현하라.
"""


def dfs_recursive(graph: dict, start: int, visited: set = None) -> list:
    # 첫 호출 시 visited set 초기화
    if visited is None:
        visited = set()

    # 현재 노드를 방문 처리
    visited.add(start)

    # 방문 순서 리스트에 현재 노드 추가
    order = [start]

    # 현재 노드의 인접 노드를 순회
    for neighbor in graph.get(start, []):
        # 방문하지 않은 노드만 재귀 탐색
        if neighbor not in visited:
            # 재귀 호출 결과를 방문 순서에 추가
            order.extend(dfs_recursive(graph, neighbor, visited))

    # 방문 순서 반환
    return order


def dfs_iterative(graph: dict, start: int) -> list:
    # 방문 기록용 set
    visited = set()

    # DFS에 사용할 스택 (LIFO)
    stack = [start]

    # 방문 순서 저장 리스트
    order = []

    # 스택이 빌 때까지 반복
    while stack:
        # 스택의 맨 위에서 노드를 꺼냄
        node = stack.pop()

        # 이미 방문한 노드면 건너뜀
        if node in visited:
            continue

        # 방문 처리
        visited.add(node)
        order.append(node)

        # 인접 노드를 역순으로 스택에 추가 (작은 번호부터 방문하기 위해)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    # 방문 순서 반환
    return order


def dfs_all_paths(graph: dict, start: int, end: int) -> list:
    # 시작에서 끝까지의 모든 경로를 찾는 DFS
    all_paths = []

    # 스택에 (현재 노드, 경로) 쌍을 저장
    stack = [(start, [start])]

    # 스택이 빌 때까지 반복
    while stack:
        # 현재 노드와 경로를 꺼냄
        node, path = stack.pop()

        # 목표 노드에 도달하면 경로를 결과에 추가
        if node == end:
            all_paths.append(path)
            continue

        # 인접 노드 탐색
        for neighbor in graph.get(node, []):
            # 현재 경로에 포함되지 않은 노드만 탐색 (순환 방지)
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    # 모든 경로 반환
    return all_paths


# === 실행 예제 ===
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1, 5],
        4: [1, 2, 5],
        5: [3, 4]
    }

    print("=== DFS Recursive ===")
    print(f"방문 순서: {dfs_recursive(graph, 0)}")

    print("\n=== DFS Iterative ===")
    print(f"방문 순서: {dfs_iterative(graph, 0)}")

    print("\n=== All Paths (0 → 5) ===")
    paths = dfs_all_paths(graph, 0, 5)
    for i, path in enumerate(paths, 1):
        print(f"  경로 {i}: {' → '.join(map(str, path))}")
