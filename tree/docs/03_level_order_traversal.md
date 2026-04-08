# 03. Level Order Traversal (레벨 순회)

## 문제 정의

이진 트리가 주어졌을 때, 레벨별로 노드 값을 그룹화하여 반환하라. 같은 레벨의 노드는 왼쪽에서 오른쪽 순서로 방문한다.

---

## 접근법 1: BFS를 이용한 레벨 순회

큐를 사용하여 한 레벨씩 처리합니다.

```python
def level_order_bfs(root: TreeNode) -> list:
```

### 라인별 설명

```python
queue = deque([root])
```
- BFS의 핵심 자료구조인 큐를 생성하고 루트를 넣습니다.

```python
while queue:
    level_size = len(queue)
    level = []
```
- **핵심**: `level_size`로 현재 레벨에 있는 노드 수를 기록합니다.
- 이 값만큼만 반복하면 정확히 한 레벨의 노드만 처리할 수 있습니다.

```python
    for _ in range(level_size):
        node = queue.popleft()
        level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```
- 현재 레벨의 노드를 하나씩 꺼내며 값을 저장합니다.
- 각 노드의 자식을 큐에 추가하면 이들은 다음 레벨에서 처리됩니다.

### 실행 예제

```
트리:     3
        / \
       9  20
         /  \
        15   7

레벨 0: queue=[3], level_size=1
  pop 3 → level=[3], push 9, 20
  result=[[3]]

레벨 1: queue=[9, 20], level_size=2
  pop 9  → level=[9]
  pop 20 → level=[9, 20], push 15, 7
  result=[[3], [9, 20]]

레벨 2: queue=[15, 7], level_size=2
  pop 15 → level=[15]
  pop 7  → level=[15, 7]
  result=[[3], [9, 20], [15, 7]]
```

---

## 접근법 2: DFS를 이용한 레벨 순회

재귀적 DFS에 깊이 정보를 전달하여 레벨별로 그룹화합니다.

```python
def level_order_dfs(root: TreeNode) -> list:
```

### 라인별 설명

```python
def dfs(node: TreeNode, depth: int) -> None:
    if not node:
        return
```
- DFS 헬퍼 함수로, 현재 깊이를 매개변수로 전달합니다.

```python
    if depth == len(result):
        result.append([])
```
- **핵심**: 새로운 레벨에 처음 도달하면 빈 리스트를 추가합니다.
- `depth`가 `result`의 길이와 같다는 것은 이 레벨이 아직 생성되지 않았다는 뜻입니다.

```python
    result[depth].append(node.val)
    dfs(node.left, depth + 1)
    dfs(node.right, depth + 1)
```
- 현재 깊이에 해당하는 레벨에 값을 추가합니다.
- 왼쪽을 먼저 탐색하므로 같은 레벨 내에서 왼→오 순서가 유지됩니다.

### 실행 예제

```
트리:     3
        / \
       9  20

dfs(3, 0) → result=[[3]]
  dfs(9, 1) → result=[[3], [9]]
  dfs(20, 1) → result=[[3], [9, 20]]

결과: [[3], [9, 20]]
```

---

## 접근법 3: 지그재그 레벨 순회

홀수 레벨은 오른쪽→왼쪽, 짝수 레벨은 왼쪽→오른쪽으로 순회합니다.

```python
def zigzag_level_order(root: TreeNode) -> list:
```

### 라인별 설명

```python
left_to_right = True
```
- 현재 레벨의 방향을 나타내는 플래그입니다.

```python
if left_to_right:
    level.append(node.val)
else:
    level.appendleft(node.val)
```
- **핵심**: `deque`를 사용하여 방향에 따라 삽입 위치를 결정합니다.
- 왼→오: 오른쪽에 추가 (`append`)
- 오→왼: 왼쪽에 추가 (`appendleft`)

```python
left_to_right = not left_to_right
```
- 각 레벨을 처리한 후 방향을 전환합니다.

### 실행 예제

```
트리:     3
        / \
       9  20
      /  /  \
     8  15   7

레벨 0 (→): [3]
레벨 1 (←): [20, 9]
레벨 2 (→): [8, 15, 7]

결과: [[3], [20, 9], [8, 15, 7]]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| BFS | O(N) | O(W) 큐 (W: 최대 너비) |
| DFS | O(N) | O(H) 호출 스택 |
| 지그재그 | O(N) | O(W) |

- N: 노드 수, H: 트리 높이, W: 최대 레벨 너비
- BFS가 레벨 순회의 가장 자연스러운 방법입니다.
- DFS 접근법은 재귀적이지만 결과는 동일합니다.
