# 05. Validate BST (이진 탐색 트리 검증)

## 문제 정의

이진 트리가 주어졌을 때, 모든 노드가 BST 속성을 만족하는지 검증하라.
BST 속성: 왼쪽 서브트리의 **모든** 값 < 현재 노드 값 < 오른쪽 서브트리의 **모든** 값.

---

## 접근법 1: 재귀적 범위 검증

각 노드가 허용된 값 범위 내에 있는지 확인합니다.

```python
def is_valid_bst_recursive(root: TreeNode) -> bool:
```

### 라인별 설명

```python
def validate(node: TreeNode, low: float, high: float) -> bool:
    if not node:
        return True
```
- 범위를 전달하는 헬퍼 함수입니다.
- `None` 노드는 항상 유효합니다.

```python
    if node.val <= low or node.val >= high:
        return False
```
- **핵심**: 현재 노드의 값이 허용 범위를 벗어나면 유효하지 않습니다.
- `<=`와 `>=`를 사용하는 이유: BST에서는 같은 값이 허용되지 않습니다.

```python
    left_valid = validate(node.left, low, node.val)
    right_valid = validate(node.right, node.val, high)
    return left_valid and right_valid
```
- **왼쪽 자식**: 상한을 현재 노드의 값으로 제한합니다.
- **오른쪽 자식**: 하한을 현재 노드의 값으로 제한합니다.
- 양쪽 모두 유효해야 전체가 유효합니다.

### 실행 예제

```
트리:     5
        / \
       3   7
      / \
     1   4

validate(5, -inf, inf)  → 5는 범위 내
  validate(3, -inf, 5)  → 3은 범위 내
    validate(1, -inf, 3) → 유효
    validate(4, 3, 5)    → 유효
  validate(7, 5, inf)   → 7은 범위 내 → 유효

결과: True
```

```
유효하지 않은 예:
       5
      / \
     1   4    ← 4 < 5이므로 오른쪽에 올 수 없음
        / \
       3   6

validate(4, 5, inf) → 4 <= 5 → False!
```

---

## 접근법 2: 중위 순회를 이용한 검증

BST의 중위 순회는 오름차순이어야 한다는 성질을 이용합니다.

```python
def is_valid_bst_inorder(root: TreeNode) -> bool:
```

### 라인별 설명

```python
prev = [-math.inf]
```
- 이전에 방문한 노드의 값을 저장합니다.
- 리스트로 감싸는 이유: 중첩 함수에서 외부 변수를 수정하기 위함입니다.

```python
def inorder(node: TreeNode) -> bool:
    if not node:
        return True
    if not inorder(node.left):
        return False
```
- 왼쪽 서브트리를 먼저 검증합니다.

```python
    if node.val <= prev[0]:
        return False
    prev[0] = node.val
    return inorder(node.right)
```
- **핵심**: 중위 순회에서 현재 값이 이전 값보다 크지 않으면 BST가 아닙니다.
- 이전 값을 현재 값으로 업데이트한 후 오른쪽을 검증합니다.

### 실행 예제

```
트리:     5
        / \
       3   7

중위 순회: 3 → 5 → 7
prev: -inf → 3 (3 > -inf ✓) → 5 (5 > 3 ✓) → 7 (7 > 5 ✓)

결과: True
```

---

## 접근법 3: 반복적 중위 순회

스택을 사용하여 중위 순회를 수행하며 오름차순을 확인합니다.

```python
def is_valid_bst_iterative(root: TreeNode) -> bool:
```

### 라인별 설명

```python
stack = []
current = root
prev = -math.inf
```
- 스택, 현재 노드, 이전 값을 초기화합니다.

```python
while current or stack:
    while current:
        stack.append(current)
        current = current.left
    current = stack.pop()
    if current.val <= prev:
        return False
    prev = current.val
    current = current.right
```
- 반복적 중위 순회와 동일한 구조입니다.
- 스택에서 꺼낸 노드의 값이 이전 값보다 크지 않으면 즉시 `False`를 반환합니다.
- **장점**: 조기 종료가 가능하여 전체를 순회할 필요가 없습니다.

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 재귀 범위 검증 | O(N) | O(H) 호출 스택 |
| 중위 순회 (재귀) | O(N) | O(H) 호출 스택 |
| 중위 순회 (반복) | O(N) | O(H) 스택 |

- N: 노드 수, H: 트리 높이
- 모든 접근법의 시간 복잡도는 동일하지만, 반복적 방법이 조기 종료에 유리합니다.
- **주의**: 단순히 `left.val < node.val < right.val`만 확인하면 안 됩니다. 서브트리의 **모든** 값을 고려해야 합니다.
