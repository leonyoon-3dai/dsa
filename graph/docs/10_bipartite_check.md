# 10. Bipartite Graph Check (이분 그래프 판별)

## 문제 정의

무방향 그래프가 이분 그래프(Bipartite Graph)인지 판별하라. (LeetCode 785)

**이분 그래프**: 그래프의 모든 노드를 두 그룹으로 나누어, 모든 간선이 서로 다른 그룹의 노드를 연결하도록 할 수 있는 그래프.

---

## 접근법 1: BFS (2-Coloring)

```python
def is_bipartite_bfs(graph: dict, num_nodes: int) -> tuple:
```

### 라인별 설명

```python
color = [-1] * num_nodes
```
- 각 노드의 색상: `-1`=미방문, `0`=그룹A, `1`=그룹B
- 이분 그래프 판별 = **2색 칠하기(2-coloring)** 문제와 동일합니다.

```python
color[start] = 0
queue = deque([start])
```
- 시작 노드를 그룹A(0)로 칠하고 BFS를 시작합니다.

```python
if color[neighbor] == -1:
    color[neighbor] = 1 - color[node]
    queue.append(neighbor)
elif color[neighbor] == color[node]:
    return False, []
```
- 미방문 노드: 현재 노드와 **반대 색**으로 칠합니다 (`1 - color[node]`).
- 이미 칠해진 노드가 현재 노드와 **같은 색**이면 → 이분 그래프 아님.

### 실행 예제

```
정사각형 그래프: 0-1-2-3-0

color[0] = 0 (A)
color[1] = 1 (B)  ← 0의 반대
color[2] = 0 (A)  ← 1의 반대
color[3] = 1 (B)  ← 2의 반대

3과 0: color[3]=1 ≠ color[0]=0 → OK!
→ 이분 그래프 ✓

삼각형 그래프: 0-1-2-0

color[0] = 0 (A)
color[1] = 1 (B)  ← 0의 반대
color[2] = 0 (A)  ← 1의 반대

2와 0: color[2]=0 == color[0]=0 → 충돌!
→ 이분 그래프 X
```

---

## 접근법 2: DFS (2-Coloring)

```python
def is_bipartite_dfs(graph: dict, num_nodes: int) -> tuple:
```

### 라인별 설명

```python
def dfs(node: int, c: int) -> bool:
    color[node] = c
    for neighbor in graph.get(node, []):
        if color[neighbor] == -1:
            if not dfs(neighbor, 1 - c):
                return False
        elif color[neighbor] == c:
            return False
    return True
```
- BFS와 동일한 로직을 재귀 DFS로 구현합니다.
- 인접 노드를 반대 색으로 재귀 탐색합니다.

---

## 이분 그래프의 성질

- **홀수 길이 사이클이 없으면 이분 그래프**입니다.
- 트리는 항상 이분 그래프입니다 (사이클이 없으므로).
- 짝수 길이 사이클만 있으면 이분 그래프입니다.

## 활용 사례

- 매칭 문제 (작업 배정, 면접 스케줄링)
- 그래프 2-색 칠하기
- 충돌 검사 (두 그룹으로 분리 가능한지)

---

## 복잡도

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) 호출 스택 |
