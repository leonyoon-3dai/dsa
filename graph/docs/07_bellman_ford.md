# 07. Bellman-Ford (벨만-포드)

## 문제 정의

가중치가 있는 방향 그래프에서 시작 노드로부터 모든 노드까지의 최단 거리를 구하라.
음수 가중치 순환이 있는 경우 이를 탐지하라.

---

## 접근법: Edge Relaxation 반복

```python
def bellman_ford(num_nodes: int, edges: list, start: int) -> tuple:
```

### 라인별 설명

```python
distances = [float('inf')] * num_nodes
distances[start] = 0
```
- 시작 노드를 0, 나머지를 무한대로 초기화합니다.

```python
for i in range(num_nodes - 1):
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            distances[v] = distances[u] + w
```
- **(V-1)번** 모든 간선을 반복하며 **완화(relaxation)**합니다.
- **왜 V-1번?**: 최단 경로는 최대 V-1개의 간선을 포함하므로, V-1번이면 모든 최단 경로가 확정됩니다.

```python
updated = False
...
if not updated:
    break
```
- 조기 종료 최적화: 한 번의 반복에서 업데이트가 없으면 이미 모든 최단 거리가 확정된 것입니다.

```python
# V번째 반복
for u, v, w in edges:
    if distances[u] != float('inf') and distances[u] + w < distances[v]:
        has_negative_cycle = True
```
- V-1번 반복 후에도 거리가 줄어들 수 있다면 → **음수 순환 존재**
- 음수 순환이 있으면 최단 거리가 -∞로 발산합니다.

### 실행 예제

```
간선: (0,1,4), (0,2,5), (1,2,-3), (2,3,4), (3,1,-1), (1,3,6)

초기: [0, INF, INF, INF]

반복 1: (0,1,4)→d[1]=4, (0,2,5)→d[2]=5, (1,2,-3)→d[2]=1, (2,3,4)→d[3]=5
        결과: [0, 4, 1, 5]

반복 2: (3,1,-1)→d[1]=4 (변화없음), (1,2,-3)→d[2]=1 (변화없음)
        결과: [0, 4, 1, 5]

최종: [0, 4, 1, 5]
```

---

## Dijkstra vs Bellman-Ford

| | Dijkstra | Bellman-Ford |
|--|----------|-------------|
| 음수 가중치 | X (사용 불가) | O (처리 가능) |
| 음수 순환 감지 | X | O |
| 시간 복잡도 | O((V+E) log V) | O(V × E) |
| 구현 | 최소 힙 필요 | 간선 리스트만 필요 |

## 복잡도

| | 시간 복잡도 | 공간 복잡도 |
|--|------------|------------|
| Bellman-Ford | O(V × E) | O(V) |
