# 10. Balanced Binary Tree (균형 이진 트리)

## 문제 정의

이진 트리가 주어졌을 때, 높이 균형(height-balanced)인지 확인하라.
높이 균형 트리: 모든 노드에서 왼쪽과 오른쪽 서브트리의 높이 차이가 1 이하인 트리.

---

## 접근법 1: 탑다운 방식

각 노드에서 양쪽 서브트리의 높이를 개별적으로 계산합니다.

```python
def is_balanced_top_down(root: TreeNode) -> bool:
```

### 라인별 설명

```python
def height(node: TreeNode) -> int:
    if not node:
        return 0
    return max(height(node.left), height(node.right)) + 1
```
- 노드의 높이를 재귀적으로 계산하는 함수입니다.

```python
if not root:
    return True
left_h = height(root.left)
right_h = height(root.right)
if abs(left_h - right_h) > 1:
    return False
```
- 현재 노드에서 양쪽 높이 차이가 1을 초과하면 불균형입니다.

```python
left_balanced = is_balanced_top_down(root.left)
right_balanced = is_balanced_top_down(root.right)
return left_balanced and right_balanced
```
- 현재 노드가 균형이어도 자식 노드들도 균형인지 재귀적으로 확인합니다.
- **단점**: 각 노드에서 `height()`를 호출하므로 높이 계산이 중복됩니다.

### 실행 예제

```
트리:     3
        / \
       9  20
         /  \
        15   7

is_balanced(3):
  height(9) = 1, height(20) = 2
  |1 - 2| = 1 ≤ 1 ✓
  is_balanced(9):
    height(None) = 0, height(None) = 0
    |0 - 0| = 0 ≤ 1 ✓ → True
  is_balanced(20):
    height(15) = 1, height(7) = 1
    |1 - 1| = 0 ≤ 1 ✓ → True

결과: True
```

```
불균형 트리:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

is_balanced(1):
  height(왼쪽) = 3, height(오른쪽) = 1
  |3 - 1| = 2 > 1 → False!
```

---

## 접근법 2: 바텀업 방식 (최적)

높이 계산과 균형 확인을 한 번의 DFS로 동시에 수행합니다.

```python
def is_balanced_bottom_up(root: TreeNode) -> bool:
```

### 라인별 설명

```python
def check(node: TreeNode) -> int:
    if not node:
        return 0
```
- 높이를 반환하되, 불균형이면 -1을 반환하는 함수입니다.

```python
    left_h = check(node.left)
    if left_h == -1:
        return -1
    right_h = check(node.right)
    if right_h == -1:
        return -1
```
- **핵심**: 서브트리가 불균형(-1)이면 즉시 -1을 전파합니다.
- 조기 종료: 불균형을 발견하면 나머지 탐색을 건너뜁니다.

```python
    if abs(left_h - right_h) > 1:
        return -1
    return max(left_h, right_h) + 1
```
- 현재 노드에서 높이 차이가 1을 초과하면 -1을 반환합니다.
- 균형이면 정상적인 높이를 반환합니다.

```python
return check(root) != -1
```
- 최종 결과가 -1이 아니면 전체 트리가 균형입니다.

### 실행 예제

```
트리:     3
        / \
       9  20
         /  \
        15   7

check(9) = 1
check(15) = 1, check(7) = 1
check(20) = max(1,1)+1 = 2, |1-1|=0 ✓
check(3) = max(1,2)+1 = 3, |1-2|=1 ✓

결과: 3 ≠ -1 → True
```

```
불균형 트리:
   1
  /
 2
/
3

check(3) = 1
check(2) = 2, |1-0|=1 ✓
check(1) = |2-0|=2 > 1 → -1!

결과: -1 → False
```

---

## 접근법 3: 반복적 후위 순회

스택을 사용하여 후위 순회로 높이를 계산합니다.

```python
def is_balanced_iterative(root: TreeNode) -> bool:
```

### 라인별 설명

```python
heights = {}
stack = [(root, False)]
```
- `heights`: 각 노드의 높이를 저장하는 딕셔너리.
- `(node, False)`: 자식을 아직 처리하지 않은 상태.

```python
if visited:
    left_h = heights.get(id(node.left), 0) if node.left else 0
    right_h = heights.get(id(node.right), 0) if node.right else 0
    if abs(left_h - right_h) > 1:
        return False
    heights[id(node)] = max(left_h, right_h) + 1
```
- 후위 순회: 자식들이 먼저 처리된 후 부모의 높이를 계산합니다.
- 불균형을 발견하면 즉시 `False`를 반환합니다.

```python
else:
    stack.append((node, True))
    if node.right:
        stack.append((node.right, False))
    if node.left:
        stack.append((node.left, False))
```
- 현재 노드를 방문 표시 후 다시 스택에 넣고, 자식들을 추가합니다.

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 탑다운 | O(N log N) | O(H) 호출 스택 |
| 바텀업 | O(N) | O(H) 호출 스택 |
| 반복적 | O(N) | O(N) heights 저장 |

- N: 노드 수, H: 트리 높이
- **탑다운이 느린 이유**: 각 노드에서 height()를 호출하여 높이를 중복 계산합니다. 균형 트리에서 각 레벨의 노드 수 x 높이 계산 = O(N log N).
- **바텀업이 최적인 이유**: 한 번의 DFS로 높이 계산과 균형 확인을 동시에 수행합니다.
- 면접에서는 바텀업 방식을 사용하는 것이 좋습니다.
