# 08. Diameter of Binary Tree (이진 트리 지름)

## 문제 정의

이진 트리의 지름을 구하라. 지름은 임의의 두 노드 사이의 최장 경로의 간선 수이다.
이 경로는 루트를 지나지 않을 수도 있다.

---

## 접근법 1: 전역 변수를 이용한 DFS

높이를 계산하면서 동시에 지름을 추적합니다.

```python
def diameter_global_variable(root: TreeNode) -> int:
```

### 라인별 설명

```python
diameter = [0]
```
- 지름의 최댓값을 저장할 변수입니다. 리스트로 감싸는 이유: 중첩 함수에서 수정하기 위함입니다.

```python
def height(node: TreeNode) -> int:
    if not node:
        return 0
    left_h = height(node.left)
    right_h = height(node.right)
```
- 각 노드에서 왼쪽과 오른쪽 서브트리의 높이를 재귀적으로 구합니다.

```python
    diameter[0] = max(diameter[0], left_h + right_h)
    return max(left_h, right_h) + 1
```
- **핵심**: 현재 노드를 경유하는 경로 길이 = 왼쪽 높이 + 오른쪽 높이.
- 이 값이 지금까지의 최대 지름보다 크면 갱신합니다.
- 반환값은 현재 노드의 높이 (더 깊은 쪽 + 1)입니다.
- **중요**: 지름은 반드시 루트를 지나지 않습니다. 각 노드에서 경유하는 경로를 모두 확인해야 합니다.

### 실행 예제

```
트리:     1
        / \
       2   3
      / \
     4   5

height(4) = 1, height(5) = 1
height(2): left=1, right=1, diameter=max(0, 1+1)=2, return 2
height(3) = 1
height(1): left=2, right=1, diameter=max(2, 2+1)=3, return 3

결과: 3 (경로: 4→2→1→3 또는 5→2→1→3)
```

---

## 접근법 2: 튜플 반환 DFS

전역 변수 없이 (높이, 지름)을 함께 반환합니다.

```python
def diameter_return_tuple(root: TreeNode) -> int:
```

### 라인별 설명

```python
def dfs(node: TreeNode) -> tuple:
    if not node:
        return (0, 0)
```
- 각 노드에서 (높이, 지름)을 반환합니다.

```python
    left_h, left_d = dfs(node.left)
    right_h, right_d = dfs(node.right)
```
- 왼쪽과 오른쪽 서브트리의 높이와 지름을 구합니다.

```python
    current_h = max(left_h, right_h) + 1
    through_current = left_h + right_h
    current_d = max(left_d, right_d, through_current)
    return (current_h, current_d)
```
- `current_h`: 현재 노드의 높이
- `through_current`: 현재 노드를 지나는 경로의 길이
- `current_d`: 세 후보 중 최댓값이 현재까지의 지름
  - 왼쪽 서브트리의 지름
  - 오른쪽 서브트리의 지름
  - 현재 노드를 경유하는 경로

### 실행 예제

```
트리:     1
        / \
       2   3
      / \
     4   5

dfs(4) = (1, 0)
dfs(5) = (1, 0)
dfs(2) = (2, max(0, 0, 1+1)) = (2, 2)
dfs(3) = (1, 0)
dfs(1) = (3, max(2, 0, 2+1)) = (3, 3)

결과: 3
```

---

## 접근법 3: 반복적 후위 순회

스택을 사용한 후위 순회로 높이를 바텀업 방식으로 계산합니다.

```python
def diameter_bottom_up(root: TreeNode) -> int:
```

### 라인별 설명

```python
heights = {}
diameter = 0
stack = [(root, False)]
```
- `heights`: 각 노드의 높이를 저장하는 딕셔너리.
- `(node, False)`: 아직 자식을 처리하지 않은 노드.

```python
if visited:
    left_h = heights.get(id(node.left), 0) if node.left else 0
    right_h = heights.get(id(node.right), 0) if node.right else 0
    heights[id(node)] = max(left_h, right_h) + 1
    diameter = max(diameter, left_h + right_h)
```
- 자식이 모두 처리된 후 (후위) 현재 노드의 높이를 계산합니다.
- `id(node)`를 키로 사용하여 노드를 고유하게 식별합니다.

```python
else:
    stack.append((node, True))
    if node.right:
        stack.append((node.right, False))
    if node.left:
        stack.append((node.left, False))
```
- 현재 노드를 방문 표시 후 다시 넣고, 자식들을 스택에 추가합니다.
- 왼쪽과 오른쪽 자식이 먼저 처리되어야 하므로 후위 순회 순서를 보장합니다.

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 전역 변수 DFS | O(N) | O(H) 호출 스택 |
| 튜플 반환 DFS | O(N) | O(H) 호출 스택 |
| 반복적 후위 순회 | O(N) | O(N) heights 저장 |

- N: 노드 수, H: 트리 높이
- 지름은 반드시 루트를 지나는 것은 아닙니다. 모든 노드를 확인해야 합니다.
- 높이 계산과 지름 갱신을 한 번의 DFS로 동시에 수행하는 것이 핵심입니다.
