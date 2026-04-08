# 04. Maximum Depth of Binary Tree (최대 깊이)

## 문제 정의

이진 트리가 주어졌을 때, 루트에서 가장 먼 리프 노드까지의 경로 길이(깊이)를 구하라.

---

## 접근법 1: 재귀적 DFS

트리의 높이를 재귀적으로 계산합니다.

```python
def max_depth_recursive(root: TreeNode) -> int:
```

### 라인별 설명

```python
if not root:
    return 0
```
- 기저 조건: 노드가 `None`이면 깊이는 0입니다.

```python
left_depth = max_depth_recursive(root.left)
right_depth = max_depth_recursive(root.right)
return max(left_depth, right_depth) + 1
```
- 왼쪽과 오른쪽 서브트리의 깊이를 각각 구합니다.
- **핵심**: 더 깊은 쪽의 값에 1(현재 노드)을 더하면 현재 노드의 깊이입니다.
- 재귀가 리프 노드부터 올라오면서 깊이를 누적합니다.

### 실행 예제

```
트리:     3
        / \
       9  20
         /  \
        15   7

max_depth(15) = 1, max_depth(7) = 1
max_depth(20) = max(1, 1) + 1 = 2
max_depth(9) = 1
max_depth(3) = max(1, 2) + 1 = 3

결과: 3
```

---

## 접근법 2: BFS (레벨 순회)

BFS로 레벨 수를 세면 그것이 곧 최대 깊이입니다.

```python
def max_depth_iterative_bfs(root: TreeNode) -> int:
```

### 라인별 설명

```python
depth = 0
queue = deque([root])
```
- 깊이 카운터를 0으로 초기화하고 큐에 루트를 넣습니다.

```python
while queue:
    level_size = len(queue)
    depth += 1
    for _ in range(level_size):
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```
- 각 레벨을 처리할 때마다 `depth`를 1 증가시킵니다.
- **핵심**: 모든 레벨을 처리하면 `depth`가 최대 깊이가 됩니다.

### 실행 예제

```
트리:     3
        / \
       9  20

레벨 1: [3] → depth=1, push 9, 20
레벨 2: [9, 20] → depth=2, push 없음
큐 비었음 → 결과: 2
```

---

## 접근법 3: 반복적 DFS (스택 사용)

스택에 (노드, 깊이) 쌍을 저장하여 DFS를 수행합니다.

```python
def max_depth_iterative_dfs(root: TreeNode) -> int:
```

### 라인별 설명

```python
max_d = 0
stack = [(root, 1)]
```
- 루트의 깊이를 1로 시작합니다.

```python
while stack:
    node, depth = stack.pop()
    max_d = max(max_d, depth)
```
- 각 노드를 방문할 때마다 최대 깊이를 갱신합니다.

```python
    if node.left:
        stack.append((node.left, depth + 1))
    if node.right:
        stack.append((node.right, depth + 1))
```
- 자식 노드에 현재 깊이 + 1을 전달합니다.
- 리프 노드에 도달했을 때의 깊이가 후보가 됩니다.

### 실행 예제

```
트리:     3
        / \
       9  20

stack: [(3,1)]
pop (3,1) → max_d=1, push (9,2), (20,2)
pop (20,2) → max_d=2
pop (9,2) → max_d=2

결과: 2
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 재귀 DFS | O(N) | O(H) 호출 스택 |
| BFS | O(N) | O(W) 큐 |
| 반복 DFS | O(N) | O(H) 스택 |

- N: 노드 수, H: 트리 높이, W: 최대 너비
- 재귀 DFS가 가장 간결하고 직관적입니다.
- 치우친 트리(skewed tree)에서는 H = N이 되어 공간이 O(N)까지 증가할 수 있습니다.
