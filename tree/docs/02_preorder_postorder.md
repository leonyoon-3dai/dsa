# 02. Preorder & Postorder Traversal (전위/후위 순회)

## 문제 정의

이진 트리가 주어졌을 때, 전위 순회(루트 → 왼쪽 → 오른쪽)와 후위 순회(왼쪽 → 오른쪽 → 루트)를 수행하여 노드 값을 순서대로 반환하라.

---

## 접근법 1: 재귀적 전위 순회

```python
def preorder_recursive(root: TreeNode) -> list:
```

### 라인별 설명

```python
def helper(node: TreeNode) -> None:
    if not node:
        return
    result.append(node.val)
    helper(node.left)
    helper(node.right)
```
- **전위 순회**: 현재 노드를 **먼저** 방문한 후 왼쪽, 오른쪽 서브트리를 순회합니다.
- 중위 순회와 비교하면 `result.append` 위치만 다릅니다.

### 실행 예제

```
트리:     1
        / \
       2   3
      / \
     4   5

helper(1) → result에 1 추가
          → helper(2) → result에 2 추가
                      → helper(4) → result에 4 추가
                      → helper(5) → result에 5 추가
          → helper(3) → result에 3 추가

결과: [1, 2, 4, 5, 3]
```

---

## 접근법 2: 반복적 전위 순회 (스택 사용)

```python
def preorder_iterative(root: TreeNode) -> list:
```

### 라인별 설명

```python
stack = [root]
while stack:
    node = stack.pop()
    result.append(node.val)
```
- 스택에서 노드를 꺼내 바로 방문합니다.

```python
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
```
- **핵심**: 오른쪽 자식을 먼저 스택에 넣습니다.
- 스택은 LIFO이므로 왼쪽 자식이 나중에 들어가서 먼저 처리됩니다.
- 이렇게 하면 전위 순회의 "루트 → 왼쪽 → 오른쪽" 순서가 보장됩니다.

### 실행 예제

```
트리:     1
        / \
       2   3

스택: [1]
pop 1 → result=[1], push 3, push 2
스택: [3, 2]
pop 2 → result=[1,2]
스택: [3]
pop 3 → result=[1,2,3]

결과: [1, 2, 3]
```

---

## 접근법 3: 재귀적 후위 순회

```python
def postorder_recursive(root: TreeNode) -> list:
```

### 라인별 설명

```python
def helper(node: TreeNode) -> None:
    if not node:
        return
    helper(node.left)
    helper(node.right)
    result.append(node.val)
```
- **후위 순회**: 왼쪽, 오른쪽 서브트리를 **먼저** 순회한 후 현재 노드를 마지막에 방문합니다.
- 자식들을 모두 처리한 뒤 부모를 처리하므로 **삭제** 연산에 적합합니다.

### 실행 예제

```
트리:     1
        / \
       2   3
      / \
     4   5

helper(4) → result=[4]
helper(5) → result=[4,5]
helper(2) → result=[4,5,2]
helper(3) → result=[4,5,2,3]
helper(1) → result=[4,5,2,3,1]

결과: [4, 5, 2, 3, 1]
```

---

## 접근법 4: 반복적 후위 순회 (두 개의 스택)

```python
def postorder_iterative(root: TreeNode) -> list:
```

### 라인별 설명

```python
stack1 = [root]
stack2 = []
```
- 첫 번째 스택은 탐색용, 두 번째 스택은 결과의 역순 저장용입니다.

```python
while stack1:
    node = stack1.pop()
    stack2.append(node)
    if node.left:
        stack1.append(node.left)
    if node.right:
        stack1.append(node.right)
```
- stack1에서 꺼낸 노드를 stack2에 넣습니다.
- **핵심**: 왼쪽을 먼저 push하면 오른쪽이 먼저 pop되어 stack2에 들어갑니다.
- stack2를 역순으로 읽으면 후위 순회 결과가 됩니다.

```python
while stack2:
    result.append(stack2.pop().val)
```
- stack2를 pop하면 후위 순회 순서 (왼쪽 → 오른쪽 → 루트)가 됩니다.

### 실행 예제

```
트리:     1
        / \
       2   3

stack1: [1]
pop 1 → stack2=[1], push 2, push 3
stack1: [2, 3]
pop 3 → stack2=[1, 3]
pop 2 → stack2=[1, 3, 2]

stack2 pop: 2, 3, 1 → result=[2, 3, 1]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 전위 재귀 | O(N) | O(H) 호출 스택 |
| 전위 반복 | O(N) | O(H) 스택 |
| 후위 재귀 | O(N) | O(H) 호출 스택 |
| 후위 반복 (두 스택) | O(N) | O(N) |

- N: 노드 수, H: 트리 높이
- 전위 순회는 **직렬화**, 후위 순회는 **삭제/수식 평가**에 자주 사용됩니다.
