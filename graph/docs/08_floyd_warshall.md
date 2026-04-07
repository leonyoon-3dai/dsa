# 08. Floyd-Warshall (플로이드-워셜)

## 문제 정의

가중치가 있는 그래프에서 모든 노드 쌍 (i, j)에 대해 최단 거리를 구하라.

---

## 접근법: 중간 노드 경유 (DP)

```python
def floyd_warshall(num_nodes: int, edges: list) -> tuple:
```

### 라인별 설명

```python
dist = [[INF] * num_nodes for _ in range(num_nodes)]
for i in range(num_nodes):
    dist[i][i] = 0
for u, v, w in edges:
    dist[u][v] = w
```
- 2D 거리 행렬 초기화:
  - 자기 자신까지 거리: 0
  - 직접 연결된 노드: 간선 가중치
  - 나머지: 무한대

```python
for k in range(num_nodes):
    for i in range(num_nodes):
        for j in range(num_nodes):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]
```
- **핵심 아이디어**: 노드 k를 중간에 경유하는 것이 더 짧은지 확인합니다.
- `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
- **k가 가장 바깥 루프**인 것이 중요합니다:
  - k=0: 노드 0을 경유하는 경로 갱신
  - k=1: 노드 0,1을 경유하는 경로 갱신
  - ...
  - k=V-1: 모든 노드를 경유하는 경로 갱신 완료

```python
has_negative_cycle = any(dist[i][i] < 0 for i in range(num_nodes))
```
- 자기 자신으로 돌아오는 거리가 음수면 → **음수 순환 존재**

### 실행 예제

```
간선: (0,1,3), (0,2,8), (1,2,2), (1,3,5), (2,3,1), (3,0,2)

초기 거리 행렬:
     0    1    2    3
0: [ 0,   3,   8, INF]
1: [INF,  0,   2,   5]
2: [INF,INF,   0,   1]
3: [ 2, INF, INF,   0]

k=0 후: 3→1 = 3→0→1 = 2+3 = 5
k=1 후: 0→2 = 0→1→2 = 3+2 = 5
k=2 후: 0→3 = 0→2→3 = 5+1 = 6, 1→3 = 1→2→3 = 2+1 = 3
k=3 후: 1→0 = 1→3→0 = 3+2 = 5, 2→0 = 2→3→0 = 1+2 = 3

최종:
     0  1  2  3
0: [ 0, 3, 5, 6]
1: [ 5, 0, 2, 3]
2: [ 3, 6, 0, 1]
3: [ 2, 5, 7, 0]
```

---

## 경로 복원

```python
next_node[i][j] = next_node[i][k]
```
- `next_node[i][j]`: i에서 j로 가는 최단 경로에서 i 다음에 방문할 노드
- 경로 복원: i → next[i][j] → next[next[i][j]][j] → ... → j

---

## 비교: 단일 출발점 vs 모든 쌍

| | Dijkstra × V회 | Floyd-Warshall |
|--|----------------|----------------|
| 시간 복잡도 | O(V(V+E) log V) | O(V³) |
| 구현 복잡도 | 높음 | 낮음 (3중 루프) |
| 음수 가중치 | X | O |
| 적합한 경우 | 희소 그래프 | 밀집 그래프 |

## 복잡도

| | 시간 복잡도 | 공간 복잡도 |
|--|------------|------------|
| Floyd-Warshall | O(V³) | O(V²) |
