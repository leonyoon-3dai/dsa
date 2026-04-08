# 07. BST Insert/Search/Delete (이진 탐색 트리 연산)

## 문제 정의

이진 탐색 트리(BST)에서 노드를 삽입, 검색, 삭제하는 함수를 구현하라.
BST 속성: 모든 노드에 대해 왼쪽 자손 < 현재 노드 < 오른쪽 자손.

---

## 접근법 1: 재귀적 BST 검색

BST 속성을 이용하여 탐색 방향을 결정합니다.

```python
def bst_search_recursive(root: TreeNode, target: int) -> TreeNode:
```

### 라인별 설명

```python
if not root or root.val == target:
    return root
```
- 노드가 없거나 목표값을 찾으면 반환합니다.

```python
if target < root.val:
    return bst_search_recursive(root.left, target)
return bst_search_recursive(root.right, target)
```
- **핵심**: 목표값이 현재보다 작으면 왼쪽, 크면 오른쪽으로 탐색합니다.
- 매 단계에서 탐색 공간이 절반으로 줄어듭니다.

### 실행 예제

```
BST:      5
        / \
       3   7
      / \
     1   4

search(5, 4):
  4 < 5 → search(3, 4)
  4 > 3 → search(4, 4)
  4 == 4 → 찾음!
```

---

## 접근법 2: 반복적 BST 검색

재귀 대신 반복문으로 탐색합니다.

```python
def bst_search_iterative(root: TreeNode, target: int) -> TreeNode:
```

### 라인별 설명

```python
while current:
    if current.val == target:
        return current
    elif target < current.val:
        current = current.left
    else:
        current = current.right
```
- 재귀와 동일한 로직이지만 스택 오버플로 위험이 없습니다.
- **장점**: 꼬리 재귀를 반복으로 변환한 형태로 더 효율적입니다.

---

## BST 삽입

```python
def bst_insert(root: TreeNode, val: int) -> TreeNode:
```

### 라인별 설명

```python
if not root:
    return TreeNode(val)
```
- 빈 위치에 도달하면 새 노드를 생성하여 반환합니다.

```python
if val < root.val:
    root.left = bst_insert(root.left, val)
elif val > root.val:
    root.right = bst_insert(root.right, val)
return root
```
- **핵심**: 삽입 위치를 재귀적으로 찾아 내려갑니다.
- `root.left = bst_insert(...)` 형태로 부모-자식 연결을 유지합니다.
- 같은 값은 삽입하지 않습니다 (중복 방지).

### 실행 예제

```
빈 BST에 [5, 3, 7, 1, 4] 삽입:

insert(None, 5) → [5]
insert(5, 3) → 3 < 5, 왼쪽으로 → [5(L:3)]
insert(5, 7) → 7 > 5, 오른쪽으로 → [5(L:3, R:7)]
insert(5, 1) → 1 < 5 → 1 < 3, 왼쪽으로 → [5(L:3(L:1), R:7)]
insert(5, 4) → 4 < 5 → 4 > 3, 오른쪽으로 → [5(L:3(L:1,R:4), R:7)]

결과:     5
        / \
       3   7
      / \
     1   4
```

---

## BST 삭제

```python
def bst_delete(root: TreeNode, val: int) -> TreeNode:
```

### 라인별 설명

```python
if val < root.val:
    root.left = bst_delete(root.left, val)
elif val > root.val:
    root.right = bst_delete(root.right, val)
```
- 먼저 삭제할 노드를 찾습니다.

```python
else:
    if not root.left:
        return root.right
    if not root.right:
        return root.left
```
- **경우 1**: 자식이 하나 이하인 경우 → 있는 자식(또는 None)으로 대체합니다.

```python
    successor = root.right
    while successor.left:
        successor = successor.left
    root.val = successor.val
    root.right = bst_delete(root.right, successor.val)
```
- **경우 2**: 자식이 두 개인 경우
  - 오른쪽 서브트리의 최솟값(중위 후계자)을 찾습니다.
  - 현재 노드의 값을 후계자의 값으로 대체합니다.
  - 후계자를 오른쪽 서브트리에서 삭제합니다.
  - **핵심**: 후계자는 왼쪽 자식이 없으므로 삭제가 간단합니다.

### 실행 예제

```
BST:      5
        / \
       3   7
      / \
     1   4

delete(5, 3):
  3을 찾음 → 자식이 두 개 (1, 4)
  후계자 = 4 (오른쪽 서브트리의 최솟값)
  3의 값을 4로 변경
  오른쪽에서 4를 삭제 (자식 없음)

결과:     5
        / \
       4   7
      /
     1
```

---

## 복잡도 비교

| 연산 | 평균 시간 복잡도 | 최악 시간 복잡도 | 공간 복잡도 |
|------|----------------|----------------|------------|
| 검색 (재귀) | O(log N) | O(N) | O(H) |
| 검색 (반복) | O(log N) | O(N) | O(1) |
| 삽입 | O(log N) | O(N) | O(H) |
| 삭제 | O(log N) | O(N) | O(H) |

- N: 노드 수, H: 트리 높이
- 균형 BST에서 H = O(log N), 치우친 BST에서 H = O(N)
- 최악의 경우를 방지하려면 AVL 트리나 레드-블랙 트리를 사용합니다.
