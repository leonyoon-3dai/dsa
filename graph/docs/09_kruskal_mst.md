# 09. Kruskal's MST (최소 신장 트리)

## 문제 정의

가중치가 있는 무방향 그래프에서 모든 노드를 연결하는 최소 비용의 트리(MST)를 구하라.

**MST(Minimum Spanning Tree)**: V개의 노드를 V-1개의 간선으로 연결하되, 간선 가중치 합이 최소인 트리.

---

## 핵심 자료구조: Union-Find

```python
class UnionFind:
```

### 라인별 설명

```python
self.parent = list(range(n))
self.rank = [0] * n
```
- 각 노드의 부모를 자기 자신으로 초기화합니다 (각자 독립된 집합).
- `rank`: 트리의 높이를 추적하여 균형을 유지합니다.

```python
def find(self, x: int) -> int:
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
```
- **경로 압축(Path Compression)**: 루트를 찾으면서 경로상의 모든 노드를 루트에 직접 연결합니다.
- 이후 find 연산이 거의 O(1)에 가깝게 됩니다.

```python
def union(self, x: int, y: int) -> bool:
    if root_x == root_y:
        return False
    if self.rank[root_x] < self.rank[root_y]:
        self.parent[root_x] = root_y
```
- **Union by Rank**: 낮은 트리를 높은 트리에 붙여서 트리 높이를 최소화합니다.
- 이미 같은 집합이면 `False`를 반환합니다 (순환 감지).

---

## 접근법: Kruskal's Algorithm

```python
def kruskal(num_nodes: int, edges: list) -> tuple:
```

### 라인별 설명

```python
sorted_edges = sorted(edges, key=lambda x: x[2])
```
- **간선을 가중치 기준으로 오름차순 정렬** → 그리디의 핵심

```python
for u, v, w in sorted_edges:
    if uf.union(u, v):
        mst_edges.append((u, v, w))
        total_weight += w
        if len(mst_edges) == num_nodes - 1:
            break
```
- 가장 가벼운 간선부터 확인합니다.
- 두 노드가 **다른 집합**이면 (순환이 생기지 않으면) MST에 추가합니다.
- V-1개의 간선이 모이면 MST 완성입니다.

### 실행 예제

```
간선 (정렬 후): (1,2,1), (3,5,1), (1,3,2), (3,4,2), (0,2,3), (2,4,3), (0,1,4), (2,3,4), (4,5,6)

1. (1,2,1): union(1,2) → 추가 ✓  총합: 1
2. (3,5,1): union(3,5) → 추가 ✓  총합: 2
3. (1,3,2): union(1,3) → 추가 ✓  총합: 4
4. (3,4,2): union(3,4) → 추가 ✓  총합: 6
5. (0,2,3): union(0,2) → 추가 ✓  총합: 9
   → 5개 간선 = 6-1, MST 완성!

MST 총 가중치: 9
```

---

## Kruskal vs Prim

| | Kruskal | Prim |
|--|---------|------|
| 전략 | 간선 정렬 + Union-Find | 노드 확장 + 최소 힙 |
| 시간 복잡도 | O(E log E) | O((V+E) log V) |
| 적합한 경우 | 희소 그래프 (E ≈ V) | 밀집 그래프 (E ≈ V²) |

## 복잡도

| | 시간 복잡도 | 공간 복잡도 |
|--|------------|------------|
| Kruskal + Union-Find | O(E log E) | O(V + E) |
