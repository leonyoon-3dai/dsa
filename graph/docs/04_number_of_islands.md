# 04. Number of Islands (섬의 개수)

## 문제 정의

2D 그리드에서 '1'은 땅, '0'은 물을 나타낸다.
상하좌우로 연결된 '1'들의 묶음(섬)의 개수를 구하라. (LeetCode 200)

---

## 접근법 1: BFS

```python
def num_islands_bfs(grid: list) -> int:
```

### 라인별 설명

```python
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
```
- 상하좌우 4방향을 나타내는 방향 벡터입니다.

```python
if grid[r][c] == "1" and not visited[r][c]:
    count += 1
    queue = deque([(r, c)])
    visited[r][c] = True
```
- 미방문 땅을 발견하면 새로운 섬을 카운트합니다.
- BFS를 시작하여 연결된 모든 땅을 방문 처리합니다.

```python
for dr, dc in directions:
    nr, nc = cr + dr, cc + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and not visited[nr][nc]:
        visited[nr][nc] = True
        queue.append((nr, nc))
```
- 상하좌우로 인접한 땅을 큐에 추가합니다.
- 범위 체크 + 땅인지 확인 + 미방문 확인을 모두 수행합니다.

### 실행 예제

```
그리드:
  1 1 0 0 0
  1 1 0 0 0
  0 0 1 0 0
  0 0 0 1 1

섬 1: (0,0), (0,1), (1,0), (1,1) → 좌상단 블록
섬 2: (2,2) → 가운데
섬 3: (3,3), (3,4) → 우하단

결과: 3
```

---

## 접근법 2: DFS (In-place)

```python
def num_islands_dfs(grid: list) -> int:
```

### 라인별 설명

```python
grid[r][c] = "0"
```
- **핵심 트릭**: 방문한 땅을 물('0')로 바꿔서 별도의 visited 배열 없이 구현합니다.
- 공간을 절약하지만 원본 그리드가 변경됩니다.

```python
dfs(r - 1, c)  # 위
dfs(r + 1, c)  # 아래
dfs(r, c - 1)  # 왼쪽
dfs(r, c + 1)  # 오른쪽
```
- 4방향으로 재귀 호출하여 연결된 모든 땅을 물로 변경합니다.

---

## 복잡도

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| BFS | O(M × N) | O(M × N) visited 배열 |
| DFS (in-place) | O(M × N) | O(M × N) 호출 스택 (최악) |

- M: 행 수, N: 열 수
- 2D 그리드 문제에서 BFS/DFS는 가장 기본적인 접근법입니다.
