"""
Graph Algorithm Example 8: Floyd-Warshall Algorithm
플로이드-워셜 알고리즘 - 모든 노드 쌍 간의 최단 거리를 구하는 알고리즘

Problem: 가중치가 있는 그래프에서 모든 노드 쌍 (i, j)에 대해 최단 거리를 구하라.
"""

INF = float('inf')


def floyd_warshall(num_nodes: int, edges: list) -> tuple:
    # 거리 행렬 초기화: 자기 자신은 0, 나머지는 무한대
    dist = [[INF] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        dist[i][i] = 0

    # 다음 노드 행렬 (경로 복원용)
    next_node = [[None] * num_nodes for _ in range(num_nodes)]

    # 간선 정보로 거리 행렬 초기화
    for u, v, w in edges:
        dist[u][v] = w
        next_node[u][v] = v

    # 핵심: 중간 노드 k를 거쳐가는 경로가 더 짧은지 확인
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                # i → k → j 경로가 i → j 직접 경로보다 짧으면 업데이트
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # 음수 순환 감지: 대각선에 음수 값이 있으면 음수 순환 존재
    has_negative_cycle = any(dist[i][i] < 0 for i in range(num_nodes))

    return dist, next_node, has_negative_cycle


def reconstruct_path(next_node: list, start: int, end: int) -> list:
    # 경로가 없으면 빈 리스트 반환
    if next_node[start][end] is None:
        return []

    # 경로 복원
    path = [start]
    current = start

    while current != end:
        current = next_node[current][end]
        path.append(current)

    return path


# === 실행 예제 ===
if __name__ == "__main__":
    # 간선 리스트: (출발, 도착, 가중치)
    edges = [
        (0, 1, 3),
        (0, 2, 8),
        (1, 2, 2),
        (1, 3, 5),
        (2, 3, 1),
        (3, 0, 2),
    ]
    num_nodes = 4

    print("=== Floyd-Warshall Algorithm ===")
    dist, next_node, has_negative_cycle = floyd_warshall(num_nodes, edges)

    if has_negative_cycle:
        print("음수 순환이 존재합니다!")
    else:
        print("\n최단 거리 행렬:")
        # 헤더 출력
        print(f"     {''.join(f'{j:>6}' for j in range(num_nodes))}")
        for i in range(num_nodes):
            row = ""
            for j in range(num_nodes):
                if dist[i][j] == INF:
                    row += f"{'INF':>6}"
                else:
                    row += f"{dist[i][j]:>6}"
            print(f"  {i}: {row}")

        print("\n주요 최단 경로:")
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j and dist[i][j] != INF:
                    path = reconstruct_path(next_node, i, j)
                    print(f"  {i} → {j}: {' → '.join(map(str, path))} (거리: {dist[i][j]})")
