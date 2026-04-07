"""
Graph Algorithm Example 1: BFS (Breadth-First Search)
너비 우선 탐색 - 그래프의 가장 기본적인 탐색 알고리즘

Problem: 그래프에서 시작 노드로부터 모든 노드를 너비 우선으로 방문하라.
또한 시작 노드에서 각 노드까지의 최단 거리(간선 수)를 구하라.
"""

from collections import deque


def bfs_traversal(graph: dict, start: int) -> list:
    # 방문한 노드를 기록할 set
    visited = set()

    # BFS에 사용할 큐를 deque로 생성하고 시작 노드를 넣음
    queue = deque([start])

    # 시작 노드를 방문 처리
    visited.add(start)

    # 방문 순서를 저장할 리스트
    order = []

    # 큐가 빌 때까지 반복
    while queue:
        # 큐의 앞에서 노드를 꺼냄 (FIFO)
        node = queue.popleft()

        # 방문 순서에 추가
        order.append(node)

        # 현재 노드의 모든 인접 노드를 확인
        for neighbor in graph.get(node, []):
            # 아직 방문하지 않은 노드만 처리
            if neighbor not in visited:
                # 방문 처리
                visited.add(neighbor)
                # 큐에 추가
                queue.append(neighbor)

    # 방문 순서를 반환
    return order


def bfs_shortest_distance(graph: dict, start: int) -> dict:
    # 각 노드까지의 최단 거리를 저장할 딕셔너리
    distance = {start: 0}

    # BFS 큐 생성
    queue = deque([start])

    # 큐가 빌 때까지 반복
    while queue:
        # 현재 노드를 꺼냄
        node = queue.popleft()

        # 인접 노드 탐색
        for neighbor in graph.get(node, []):
            # 아직 거리가 계산되지 않은 노드만 처리
            if neighbor not in distance:
                # 현재 노드 거리 + 1이 인접 노드까지의 최단 거리
                distance[neighbor] = distance[node] + 1
                # 큐에 추가
                queue.append(neighbor)

    # 모든 노드까지의 최단 거리를 반환
    return distance


def bfs_path(graph: dict, start: int, end: int) -> list:
    # 시작과 끝이 같으면 바로 반환
    if start == end:
        return [start]

    # 방문 여부 기록
    visited = {start}

    # 큐에 (현재 노드, 경로) 쌍을 저장
    queue = deque([(start, [start])])

    # 큐가 빌 때까지 반복
    while queue:
        # 현재 노드와 경로를 꺼냄
        node, path = queue.popleft()

        # 인접 노드 탐색
        for neighbor in graph.get(node, []):
            # 방문하지 않은 노드만 처리
            if neighbor not in visited:
                # 새로운 경로 생성
                new_path = path + [neighbor]

                # 목표 노드에 도달하면 경로 반환
                if neighbor == end:
                    return new_path

                # 방문 처리 후 큐에 추가
                visited.add(neighbor)
                queue.append((neighbor, new_path))

    # 경로가 없으면 빈 리스트 반환
    return []


# === 실행 예제 ===
if __name__ == "__main__":
    # 그래프 정의 (인접 리스트)
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1, 5],
        4: [1, 2, 5],
        5: [3, 4]
    }

    print("=== BFS Traversal ===")
    print(f"방문 순서: {bfs_traversal(graph, 0)}")

    print("\n=== BFS Shortest Distance ===")
    distances = bfs_shortest_distance(graph, 0)
    for node, dist in sorted(distances.items()):
        print(f"  노드 0 → 노드 {node}: 거리 {dist}")

    print("\n=== BFS Shortest Path ===")
    path = bfs_path(graph, 0, 5)
    print(f"  노드 0 → 노드 5: {' → '.join(map(str, path))}")
