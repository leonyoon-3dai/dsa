# 03. Dijkstra (다익스트라 최단 경로)

## 문제 정의

가중치가 있는 그래프에서 시작 노드로부터 모든 노드까지의 최단 거리를 구하라.
(음수 가중치가 없는 경우에만 사용 가능)

---

## 접근법: 최소 힙(Priority Queue) 사용

```python
def dijkstra(graph: dict, start: int) -> tuple:
```

### 라인별 설명

```python
distances = {node: float('inf') for node in graph}
distances[start] = 0
```
- 모든 노드의 거리를 무한대로, 시작 노드만 0으로 초기화합니다.

```python
min_heap = [(0, start)]
```
- 최소 힙: `(거리, 노드)` 쌍을 저장합니다.
- Python의 `heapq`는 기본적으로 최소 힙이므로 거리가 가장 짧은 노드가 먼저 나옵니다.

```python
current_dist, current_node = heapq.heappop(min_heap)
if current_node in visited:
    continue
visited.add(current_node)
```
- 가장 거리가 짧은 노드를 꺼냅니다.
- 이미 처리된 노드는 건너뜁니다 (lazy deletion).

```python
for neighbor, weight in graph[current_node]:
    new_dist = current_dist + weight
    if new_dist < distances[neighbor]:
        distances[neighbor] = new_dist
        previous[neighbor] = current_node
        heapq.heappush(min_heap, (new_dist, neighbor))
```
- **Relaxation**: 현재 노드를 거쳐가는 경로가 더 짧으면 업데이트합니다.
- 업데이트된 노드를 힙에 다시 추가합니다.

### 실행 예제

```
그래프:
  0 --(4)--> 1, 0 --(1)--> 2
  2 --(2)--> 1, 1 --(1)--> 3
  1 --(3)--> 4, 3 --(2)--> 5
  4 --(1)--> 5

시작: 0

힙: [(0,0)]
  pop (0,0): 0→1=4, 0→2=1
힙: [(1,2), (4,1)]
  pop (1,2): 2→1=3 (1보다 짧음→업데이트)
힙: [(3,1), (4,1)]
  pop (3,1): 1→3=4, 1→4=6
힙: [(4,1), (4,3), (6,4)]
  pop (4,1): 이미 방문 → skip
  pop (4,3): 3→5=6
힙: [(6,4), (6,5)]
  pop (6,4): 4→5=7 (6보다 안짧음)
  pop (6,5): 완료

결과: {0:0, 1:3, 2:1, 3:4, 4:6, 5:6}
```

---

## 경로 복원

```python
def reconstruct_path(previous: dict, start: int, end: int) -> list:
```

- `previous` 딕셔너리를 역추적하여 경로를 복원합니다.
- 끝 노드에서 시작하여 이전 노드를 따라가다가 시작 노드에 도달하면 뒤집습니다.

---

## Dijkstra vs BFS vs Bellman-Ford

| 알고리즘 | 가중치 | 음수 가중치 | 시간 복잡도 |
|---------|--------|-----------|------------|
| BFS | 없음 (또는 동일) | - | O(V + E) |
| Dijkstra | 양수만 | X | O((V+E) log V) |
| Bellman-Ford | 양수/음수 | O | O(V × E) |

## 복잡도

| | 시간 복잡도 | 공간 복잡도 |
|--|------------|------------|
| 최소 힙 사용 | O((V+E) log V) | O(V + E) |
