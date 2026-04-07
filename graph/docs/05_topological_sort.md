# 05. Topological Sort (위상 정렬)

## 문제 정의

방향 그래프에서 모든 간선 (u, v)에 대해 u가 v보다 먼저 오도록 정렬하라.
(선수과목 관계, 작업 순서 등에 활용)

**전제 조건**: 그래프는 DAG(Directed Acyclic Graph, 방향 비순환 그래프)여야 합니다.

---

## 접근법 1: Kahn's Algorithm (BFS 기반)

```python
def topological_sort_kahn(graph: dict, num_nodes: int) -> list:
```

### 라인별 설명

```python
in_degree = [0] * num_nodes
for node in range(num_nodes):
    for neighbor in graph.get(node, []):
        in_degree[neighbor] += 1
```
- **진입 차수(in-degree)**: 각 노드로 들어오는 간선의 수를 계산합니다.
- 진입 차수가 0인 노드는 선행 조건이 없으므로 먼저 처리 가능합니다.

```python
queue = deque()
for node in range(num_nodes):
    if in_degree[node] == 0:
        queue.append(node)
```
- 진입 차수가 0인 모든 노드를 큐에 넣습니다 (시작점들).

```python
node = queue.popleft()
result.append(node)
for neighbor in graph.get(node, []):
    in_degree[neighbor] -= 1
    if in_degree[neighbor] == 0:
        queue.append(neighbor)
```
- 노드를 처리하면 해당 노드에서 나가는 간선을 제거합니다 (진입 차수 감소).
- 진입 차수가 0이 된 노드를 새로 큐에 추가합니다.

```python
if len(result) != num_nodes:
    return []
```
- 모든 노드가 결과에 포함되지 않으면 순환이 존재합니다.

### 실행 예제

```
선수과목: 수학기초→미적분, 수학기초→선형대수, 미적분→확률통계, ...

진입 차수: [0, 1, 1, 1, 2, 2]  (수학기초만 0)

큐: [수학기초] → 처리 후 미적분, 선형대수의 진입 차수 감소
큐: [미적분, 선형대수] → ...

결과: 수학기초 → 미적분 → 선형대수 → 확률통계 → 머신러닝 → 딥러닝
```

---

## 접근법 2: DFS 기반

```python
def topological_sort_dfs(graph: dict, num_nodes: int) -> list:
```

### 라인별 설명

```python
state = [0] * num_nodes  # 0=미방문, 1=방문중, 2=완료
```
- 3가지 상태로 순환 감지와 위상 정렬을 동시에 수행합니다.

```python
if state[neighbor] == 1:
    has_cycle = True
    return
```
- 현재 DFS 경로에서 이미 방문중인 노드를 만나면 순환입니다.

```python
state[node] = 2
result.append(node)
```
- **후위 순서(post-order)**: 모든 후속 노드를 처리한 후에 현재 노드를 추가합니다.

```python
result.reverse()
```
- 후위 순서를 뒤집으면 위상 정렬 순서가 됩니다.

---

## 복잡도

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| Kahn's (BFS) | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |

- 두 방법 모두 동일한 복잡도이지만, Kahn's는 순환 감지가 더 직관적입니다.
- 위상 정렬의 결과는 유일하지 않을 수 있습니다 (여러 유효한 순서 존재).
