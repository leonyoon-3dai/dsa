"""
Graph Algorithm Example 9: Kruskal's MST (Minimum Spanning Tree)
크루스칼 알고리즘 - 최소 신장 트리를 구하는 그리디 알고리즘

Problem: 가중치가 있는 무방향 그래프에서 모든 노드를 연결하는
최소 비용의 트리(MST)를 구하라.
"""


class UnionFind:
    """Union-Find (Disjoint Set Union) 자료구조"""

    def __init__(self, n: int):
        # 각 노드의 부모를 자기 자신으로 초기화
        self.parent = list(range(n))
        # 각 트리의 랭크(높이)를 0으로 초기화
        self.rank = [0] * n

    def find(self, x: int) -> int:
        # 경로 압축: 루트를 찾으면서 모든 노드의 부모를 루트로 변경
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # 두 노드의 루트를 찾음
        root_x = self.find(x)
        root_y = self.find(y)

        # 이미 같은 집합이면 False 반환 (순환 발생)
        if root_x == root_y:
            return False

        # 랭크가 작은 트리를 큰 트리에 붙임 (Union by Rank)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(num_nodes: int, edges: list) -> tuple:
    # 간선을 가중치 기준으로 오름차순 정렬
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Union-Find 자료구조 초기화
    uf = UnionFind(num_nodes)

    # MST에 포함된 간선 리스트
    mst_edges = []

    # MST의 총 가중치
    total_weight = 0

    # 정렬된 간선을 순서대로 확인
    for u, v, w in sorted_edges:
        # 두 노드가 다른 집합에 속하면 (순환이 없으면)
        if uf.union(u, v):
            # MST에 간선 추가
            mst_edges.append((u, v, w))
            total_weight += w

            # MST에 V-1개의 간선이 포함되면 완성
            if len(mst_edges) == num_nodes - 1:
                break

    # (MST 간선 리스트, 총 가중치)를 반환
    return mst_edges, total_weight


# === 실행 예제 ===
if __name__ == "__main__":
    # 무방향 가중치 그래프의 간선: (노드1, 노드2, 가중치)
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (2, 4, 3),
        (3, 4, 2),
        (3, 5, 1),
        (4, 5, 6),
    ]
    num_nodes = 6

    print("=== Kruskal's MST Algorithm ===")
    print(f"\n전체 간선 ({len(edges)}개):")
    for u, v, w in edges:
        print(f"  {u} -- {v} (가중치: {w})")

    mst_edges, total_weight = kruskal(num_nodes, edges)

    print(f"\nMST 간선 ({len(mst_edges)}개):")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} (가중치: {w})")

    print(f"\nMST 총 가중치: {total_weight}")
