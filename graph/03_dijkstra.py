"""
Graph Algorithm Example 3: Dijkstra's Algorithm
다익스트라 알고리즘 - 가중치 그래프에서 최단 경로를 찾는 알고리즘

Problem: 가중치가 있는 그래프에서 시작 노드로부터 모든 노드까지의 최단 거리를 구하라.
(음수 가중치가 없는 경우에만 사용 가능)
"""

import heapq


def dijkstra(graph: dict, start: int) -> tuple:
    # 모든 노드의 거리를 무한대로 초기화
    distances = {node: float('inf') for node in graph}

    # 시작 노드의 거리를 0으로 설정
    distances[start] = 0

    # 이전 노드를 저장하여 경로 추적에 사용
    previous = {node: None for node in graph}

    # 최소 힙: (거리, 노드) 쌍을 저장
    min_heap = [(0, start)]

    # 방문 완료된 노드를 기록
    visited = set()

    # 힙이 빌 때까지 반복
    while min_heap:
        # 가장 거리가 짧은 노드를 꺼냄
        current_dist, current_node = heapq.heappop(min_heap)

        # 이미 방문한 노드면 건너뜀
        if current_node in visited:
            continue

        # 방문 처리
        visited.add(current_node)

        # 현재 노드의 인접 노드 탐색
        for neighbor, weight in graph[current_node]:
            # 새로운 거리 계산
            new_dist = current_dist + weight

            # 더 짧은 경로를 발견하면 업데이트
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                # 힙에 추가
                heapq.heappush(min_heap, (new_dist, neighbor))

    # (최단 거리 딕셔너리, 이전 노드 딕셔너리)를 반환
    return distances, previous


def reconstruct_path(previous: dict, start: int, end: int) -> list:
    # 이전 노드 정보를 역추적하여 경로를 복원
    path = []
    current = end

    # 시작 노드에 도달할 때까지 역추적
    while current is not None:
        path.append(current)
        current = previous[current]

    # 경로를 뒤집어서 시작 → 끝 순서로 만듦
    path.reverse()

    # 시작 노드가 경로의 첫 번째가 아니면 경로가 없음
    if path[0] != start:
        return []

    return path


# === 실행 예제 ===
if __name__ == "__main__":
    # 가중치 그래프 정의: {노드: [(인접 노드, 가중치), ...]}
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (3, 1), (4, 3)],
        2: [(0, 1), (1, 2), (4, 5)],
        3: [(1, 1), (5, 2)],
        4: [(1, 3), (2, 5), (5, 1)],
        5: [(3, 2), (4, 1)]
    }

    print("=== Dijkstra's Algorithm ===")
    distances, previous = dijkstra(graph, 0)

    print("\n최단 거리:")
    for node, dist in sorted(distances.items()):
        print(f"  노드 0 → 노드 {node}: {dist}")

    print("\n최단 경로:")
    for node in sorted(graph.keys()):
        if node != 0:
            path = reconstruct_path(previous, 0, node)
            print(f"  노드 0 → 노드 {node}: {' → '.join(map(str, path))} (거리: {distances[node]})")
