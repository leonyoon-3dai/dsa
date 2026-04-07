# 01. BFS (너비 우선 탐색)

## 문제 정의

그래프에서 시작 노드로부터 모든 노드를 너비 우선으로 방문하라.
또한 시작 노드에서 각 노드까지의 최단 거리(간선 수)를 구하라.

---

## 접근법 1: BFS Traversal (기본 탐색)

큐(FIFO)를 사용하여 가까운 노드부터 순서대로 방문합니다.

```python
def bfs_traversal(graph: dict, start: int) -> list:
```

### 라인별 설명

```python
visited = set()
queue = deque([start])
visited.add(start)
```
- `visited`: 방문한 노드를 기록하는 집합. 중복 방문을 방지합니다.
- `queue`: BFS의 핵심 자료구조. `deque`를 사용하여 O(1) popleft를 보장합니다.
- 시작 노드를 큐에 넣고 방문 처리합니다.

```python
while queue:
    node = queue.popleft()
    order.append(node)
```
- 큐에서 노드를 하나씩 꺼내며(FIFO) 방문 순서에 기록합니다.
- **핵심**: popleft()는 가장 먼저 들어온 노드를 꺼냅니다 → 가까운 노드부터 처리.

```python
for neighbor in graph.get(node, []):
    if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
```
- 현재 노드의 인접 노드 중 미방문 노드만 큐에 추가합니다.
- **중요**: 큐에 넣을 때 즉시 visited에 추가해야 중복 삽입을 방지합니다.

### 실행 예제

```
그래프: 0-[1,2], 1-[0,3,4], 2-[0,4], 3-[1,5], 4-[1,2,5], 5-[3,4]
시작: 0

큐: [0]         → 방문: 0, 큐에 1,2 추가
큐: [1, 2]      → 방문: 1, 큐에 3,4 추가
큐: [2, 3, 4]   → 방문: 2 (4는 이미 큐에)
큐: [3, 4]      → 방문: 3, 큐에 5 추가
큐: [4, 5]      → 방문: 4 (이미 방문한 노드 건너뜀)
큐: [5]         → 방문: 5

결과: [0, 1, 2, 3, 4, 5]
```

---

## 접근법 2: BFS Shortest Distance (최단 거리)

BFS는 가중치 없는 그래프에서 **자동으로** 최단 거리를 보장합니다.

```python
def bfs_shortest_distance(graph: dict, start: int) -> dict:
```

### 라인별 설명

```python
distance = {start: 0}
```
- 거리 딕셔너리가 visited 역할도 겸합니다. 거리가 기록된 노드 = 방문한 노드.

```python
if neighbor not in distance:
    distance[neighbor] = distance[node] + 1
```
- BFS 특성상 처음 방문할 때의 거리가 곧 최단 거리입니다.
- 현재 노드까지 거리 + 1 = 인접 노드까지 거리

---

## 접근법 3: BFS Path (최단 경로 복원)

```python
queue = deque([(start, [start])])
```
- 큐에 (노드, 경로) 쌍을 저장하여 경로를 추적합니다.

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| BFS Traversal | O(V + E) | O(V) |
| BFS Shortest Distance | O(V + E) | O(V) |
| BFS Shortest Path | O(V + E) | O(V × V) 경로 저장 |

- V: 노드 수, E: 간선 수
- BFS는 **가중치 없는 그래프**에서 최단 경로를 보장합니다.
- 가중치 있는 그래프에서는 Dijkstra를 사용해야 합니다.
