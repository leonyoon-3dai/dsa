"""
Graph Algorithm Example 7: Bellman-Ford Algorithm
벨만-포드 알고리즘 - 음수 가중치가 있는 그래프에서도 최단 경로를 찾는 알고리즘

Problem: 가중치가 있는 방향 그래프에서 시작 노드로부터 모든 노드까지의 최단 거리를 구하라.
음수 가중치 순환이 있는 경우 이를 탐지하라.
"""


def bellman_ford(num_nodes: int, edges: list, start: int) -> tuple:
    # 모든 노드의 거리를 무한대로 초기화
    distances = [float('inf')] * num_nodes

    # 시작 노드의 거리를 0으로 설정
    distances[start] = 0

    # 이전 노드 기록 (경로 복원용)
    previous = [-1] * num_nodes

    # (V-1)번 반복하여 간선을 완화(relax)
    for i in range(num_nodes - 1):
        # 모든 간선을 확인
        updated = False
        for u, v, w in edges:
            # 시작 노드에서 u까지 도달 가능하고, 더 짧은 경로가 발견되면
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                # 거리 업데이트
                distances[v] = distances[u] + w
                previous[v] = u
                updated = True

        # 이번 반복에서 업데이트가 없으면 조기 종료
        if not updated:
            break

    # V번째 반복에서도 업데이트가 가능하면 음수 순환 존재
    has_negative_cycle = False
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            has_negative_cycle = True
            break

    return distances, previous, has_negative_cycle


def reconstruct_path(previous: list, start: int, end: int) -> list:
    # 경로 역추적
    path = []
    current = end

    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    # 시작 노드에서 출발하지 않으면 경로 없음
    if path[0] != start:
        return []

    return path


# === 실행 예제 ===
if __name__ == "__main__":
    # 간선 리스트: (출발, 도착, 가중치)
    edges = [
        (0, 1, 4),
        (0, 2, 5),
        (1, 2, -3),
        (2, 3, 4),
        (3, 1, -1),
        (1, 3, 6),
    ]
    num_nodes = 4

    print("=== Bellman-Ford Algorithm ===")
    distances, previous, has_negative_cycle = bellman_ford(num_nodes, edges, 0)

    if has_negative_cycle:
        print("음수 순환이 존재합니다!")
    else:
        print("최단 거리:")
        for i in range(num_nodes):
            path = reconstruct_path(previous, 0, i)
            path_str = " → ".join(map(str, path)) if path else "경로 없음"
            print(f"  노드 0 → 노드 {i}: 거리 {distances[i]}, 경로: {path_str}")

    # 음수 순환이 있는 그래프
    print("\n=== 음수 순환 감지 ===")
    edges_negative = [
        (0, 1, 1),
        (1, 2, -1),
        (2, 0, -1),  # 0 → 1 → 2 → 0 순환의 총 가중치: 1 + (-1) + (-1) = -1
    ]

    _, _, has_neg = bellman_ford(3, edges_negative, 0)
    print(f"음수 순환 존재: {has_neg}")
