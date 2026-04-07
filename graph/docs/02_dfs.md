# 02. DFS (깊이 우선 탐색)

## 문제 정의

그래프에서 시작 노드로부터 모든 노드를 깊이 우선으로 방문하라.
재귀 방식과 스택 방식 두 가지로 구현하라.

---

## 접근법 1: DFS Recursive (재귀)

재귀 호출 스택을 이용한 자연스러운 DFS 구현입니다.

```python
def dfs_recursive(graph: dict, start: int, visited: set = None) -> list:
```

### 라인별 설명

```python
if visited is None:
    visited = set()
visited.add(start)
order = [start]
```
- 첫 호출 시 visited set을 생성합니다.
- 현재 노드를 방문 처리하고 결과에 추가합니다.

```python
for neighbor in graph.get(start, []):
    if neighbor not in visited:
        order.extend(dfs_recursive(graph, neighbor, visited))
```
- 미방문 인접 노드에 대해 재귀 호출합니다.
- **핵심**: 재귀가 깊이 들어갔다가 돌아오는 것이 DFS의 본질입니다.

### 실행 예제

```
그래프: 0-[1,2], 1-[0,3,4], 2-[0,4], 3-[1,5], 4-[1,2,5], 5-[3,4]
시작: 0

dfs(0) → 방문: 0
  dfs(1) → 방문: 1
    dfs(3) → 방문: 3
      dfs(5) → 방문: 5
        4는 미방문 → dfs(4) → 방문: 4
          2는 미방문 → dfs(2) → 방문: 2

결과: [0, 1, 3, 5, 4, 2]
```

---

## 접근법 2: DFS Iterative (반복)

명시적 스택(LIFO)을 사용합니다.

```python
def dfs_iterative(graph: dict, start: int) -> list:
```

### 라인별 설명

```python
stack = [start]
while stack:
    node = stack.pop()
```
- `stack.pop()`: 가장 최근에 추가된 노드를 꺼냅니다 (LIFO).
- BFS의 `popleft()`와 대비됩니다.

```python
for neighbor in reversed(graph.get(node, [])):
    if neighbor not in visited:
        stack.append(neighbor)
```
- `reversed`를 사용하여 작은 번호의 노드가 스택 위에 오도록 합니다.
- 이렇게 하면 재귀 방식과 동일한 방문 순서를 보장합니다.

---

## 접근법 3: All Paths (모든 경로 탐색)

```python
def dfs_all_paths(graph: dict, start: int, end: int) -> list:
```

- 스택에 `(노드, 경로)` 쌍을 저장합니다.
- `if neighbor not in path`: 현재 경로에 포함된 노드는 건너뛰어 순환을 방지합니다.
- 목표 노드 도달 시 경로를 결과에 추가하고 **탐색을 계속**합니다 (모든 경로 수집).

---

## BFS vs DFS 비교

| 특성 | BFS | DFS |
|------|-----|-----|
| 자료구조 | 큐 (FIFO) | 스택 (LIFO) |
| 최단 경로 보장 | O (가중치 없는 그래프) | X |
| 메모리 사용 | O(가장 넓은 레벨의 노드 수) | O(최대 깊이) |
| 주요 용도 | 최단 경로, 레벨 탐색 | 순환 탐지, 위상 정렬, 백트래킹 |

## 복잡도

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| DFS Recursive | O(V + E) | O(V) 호출 스택 |
| DFS Iterative | O(V + E) | O(V) 명시적 스택 |
| All Paths | O(V! × V) | O(V! × V) 경로 저장 |
