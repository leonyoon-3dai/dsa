# 06. Cycle Detection (순환 탐지)

## 문제 정의

방향 그래프와 무방향 그래프에서 순환(사이클)이 존재하는지 확인하라.

---

## 접근법 1: 방향 그래프 (3-State DFS)

```python
def has_cycle_directed(graph: dict, num_nodes: int) -> bool:
```

### 라인별 설명

```python
state = [0] * num_nodes  # 0=미방문, 1=방문중, 2=완료
```
- **3가지 상태**가 핵심입니다:
  - `0 (미방문)`: 아직 DFS가 도달하지 않은 노드
  - `1 (방문중)`: 현재 DFS 경로에 포함된 노드
  - `2 (완료)`: DFS 탐색이 끝난 노드

```python
state[node] = 1  # 방문중으로 표시
for neighbor in graph.get(node, []):
    if state[neighbor] == 1:
        return True  # 순환 발견!
```
- 현재 DFS 경로(방문중 상태)에 있는 노드를 다시 만나면 → **순환 존재**
- 완료(2) 상태의 노드를 만나는 것은 순환이 아닙니다 (다른 경로에서 이미 탐색 완료).

### 왜 2개 상태가 아닌 3개 상태가 필요한가?

```
0 → 1 → 3
0 → 2 → 3
```
- 방문/미방문 2개 상태만 사용하면, 노드 3을 두 번 만나서 순환으로 오판합니다.
- 3개 상태를 사용하면 노드 3은 `완료(2)` 상태이므로 순환이 아님을 정확히 판별합니다.

---

## 접근법 2: 무방향 그래프 (Parent 추적)

```python
def has_cycle_undirected(graph: dict, num_nodes: int) -> bool:
```

### 라인별 설명

```python
def dfs(node: int, parent: int) -> bool:
    visited[node] = True
    for neighbor in graph.get(node, []):
        if not visited[neighbor]:
            if dfs(neighbor, node):
                return True
        elif neighbor != parent:
            return True
```
- `parent`를 추적하여 **바로 직전 노드를 제외**합니다.
- 무방향 그래프에서 A-B 간선은 A→B, B→A 양방향이므로 부모를 제외하지 않으면 항상 순환으로 판단됩니다.
- 방문한 노드인데 부모가 아니면 → **순환 존재**

---

## 접근법 3: 순환 경로 찾기

```python
def find_cycle_directed(graph: dict, num_nodes: int) -> list:
```

- 순환 감지 + 경로 복원을 동시에 수행합니다.
- `parent` 배열로 각 노드의 이전 노드를 기록하여 순환 경로를 역추적합니다.

---

## 복잡도

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 방향 그래프 (3-State) | O(V + E) | O(V) |
| 무방향 그래프 (Parent) | O(V + E) | O(V) |
| 순환 경로 찾기 | O(V + E) | O(V) |
