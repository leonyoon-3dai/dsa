# 06. Lowest Common Ancestor (최소 공통 조상)

## 문제 정의

이진 트리에서 두 노드 p와 q의 최소 공통 조상(LCA)을 찾아라.
최소 공통 조상: p와 q를 모두 자손으로 가지는 가장 깊은(가장 아래의) 노드.
(노드 자체도 자신의 자손으로 간주한다.)

---

## 접근법 1: 재귀적 LCA (일반 이진 트리)

후위 순회 방식으로 양쪽 서브트리에서 p, q를 탐색합니다.

```python
def lca_binary_tree(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
```

### 라인별 설명

```python
if not root or root == p or root == q:
    return root
```
- 기저 조건: 노드가 `None`이거나 찾는 노드(p 또는 q)를 발견하면 반환합니다.

```python
left = lca_binary_tree(root.left, p, q)
right = lca_binary_tree(root.right, p, q)
```
- 왼쪽과 오른쪽 서브트리에서 각각 p 또는 q를 탐색합니다.

```python
if left and right:
    return root
return left if left else right
```
- **핵심 로직**:
  - 양쪽 모두에서 찾으면: p와 q가 서로 다른 서브트리에 있으므로 **현재 노드가 LCA**입니다.
  - 한쪽에서만 찾으면: p와 q가 같은 쪽 서브트리에 있으므로 그 결과를 전파합니다.

### 실행 예제

```
트리:      3
         / \
        5   1
       / \
      6   2

p=5, q=1:
  lca(3) → left=lca(5)=5(p 자체), right=lca(1)=1(q 자체)
         → 양쪽 모두 발견 → LCA = 3

p=5, q=6:
  lca(3) → left=lca(5)
    lca(5) → left=lca(6)=6, right=lca(2)=None
           → left만 발견 → 5 반환 (5는 p이자 6의 조상)
  right=lca(1)=None
  → left만 발견 → LCA = 5
```

---

## 접근법 2: BST에서의 LCA

BST의 정렬 속성을 활용하여 효율적으로 LCA를 찾습니다.

```python
def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
```

### 라인별 설명

```python
while current:
    if p.val < current.val and q.val < current.val:
        current = current.left
    elif p.val > current.val and q.val > current.val:
        current = current.right
    else:
        return current
```
- **핵심**: BST에서는 값의 크기를 비교하여 탐색 방향을 결정합니다.
  - p, q 모두 현재보다 작으면: LCA는 왼쪽에 있음
  - p, q 모두 현재보다 크면: LCA는 오른쪽에 있음
  - 하나는 작고 하나는 크면(또는 하나가 현재 노드): **현재 노드가 LCA**

### 실행 예제

```
BST:      6
        / \
       2   8
      / \
     0   4

p=2, q=8:
  current=6: 2 < 6 이고 8 > 6 → 서로 다른 쪽 → LCA = 6

p=2, q=4:
  current=6: 2 < 6 이고 4 < 6 → 왼쪽으로
  current=2: 2 == p → LCA = 2
```

---

## 접근법 3: 경로를 이용한 LCA

루트에서 각 노드까지의 경로를 구한 후 마지막 공통 노드를 찾습니다.

```python
def lca_with_parent(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
```

### 라인별 설명

```python
def find_path(root: TreeNode, target: TreeNode) -> list:
```
- 루트에서 대상 노드까지의 경로를 리스트로 반환합니다.

```python
path_p = find_path(root, p)
path_q = find_path(root, q)
```
- 두 노드까지의 경로를 각각 구합니다.

```python
for i in range(min(len(path_p), len(path_q))):
    if path_p[i] == path_q[i]:
        lca = path_p[i]
    else:
        break
```
- 두 경로를 앞에서부터 비교하여 마지막으로 일치하는 노드가 LCA입니다.
- 경로가 갈라지는 직전 노드가 최소 공통 조상입니다.

### 실행 예제

```
트리:      3
         / \
        5   1
       / \
      6   2

p=6, q=2:
path_p = [3, 5, 6]
path_q = [3, 5, 2]

비교: 3==3 ✓, 5==5 ✓, 6!=2 → LCA = 5
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 재귀 (일반 이진 트리) | O(N) | O(H) 호출 스택 |
| BST LCA | O(H) | O(1) 반복 |
| 경로 비교 | O(N) | O(H) 경로 저장 |

- N: 노드 수, H: 트리 높이
- BST에서는 값 비교만으로 O(H)에 LCA를 찾을 수 있습니다.
- 일반 이진 트리에서는 재귀적 방법이 가장 효율적입니다.
