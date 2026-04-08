# 01. Inorder Traversal (중위 순회)

## 문제 정의

이진 트리가 주어졌을 때, 중위 순회(왼쪽 → 루트 → 오른쪽)를 수행하여 노드 값을 순서대로 반환하라.

---

## 접근법 1: 재귀적 중위 순회

가장 직관적인 방법으로, 재귀 호출을 통해 왼쪽-루트-오른쪽 순서를 구현합니다.

```python
def inorder_recursive(root: TreeNode) -> list:
```

### 라인별 설명

```python
result = []
```
- 방문한 노드의 값을 순서대로 저장할 리스트입니다.

```python
def helper(node: TreeNode) -> None:
    if not node:
        return
```
- 기저 조건: 노드가 `None`이면 재귀를 종료합니다.

```python
    helper(node.left)
    result.append(node.val)
    helper(node.right)
```
- **핵심**: 왼쪽 서브트리를 먼저 순회한 후, 현재 노드를 방문하고, 마지막으로 오른쪽 서브트리를 순회합니다.
- 이 순서가 **중위(inorder)**의 정의입니다.

### 실행 예제

```
트리:     4
        / \
       2   6
      / \ / \
     1  3 5  7

helper(4) → helper(2) → helper(1) → helper(None) 반환
                                    → result에 1 추가
                                    → helper(None) 반환
                        → result에 2 추가
                        → helper(3) → result에 3 추가
            → result에 4 추가
            → helper(6) → helper(5) → result에 5 추가
                        → result에 6 추가
                        → helper(7) → result에 7 추가

결과: [1, 2, 3, 4, 5, 6, 7]
```

---

## 접근법 2: 반복적 중위 순회 (스택 사용)

스택을 명시적으로 사용하여 재귀를 시뮬레이션합니다.

```python
def inorder_iterative(root: TreeNode) -> list:
```

### 라인별 설명

```python
result = []
stack = []
current = root
```
- `stack`: 방문 대기 중인 노드를 저장합니다.
- `current`: 현재 탐색 중인 노드를 가리킵니다.

```python
while current or stack:
    while current:
        stack.append(current)
        current = current.left
```
- 현재 노드에서 시작하여 왼쪽 자식을 따라 계속 내려갑니다.
- 지나가는 모든 노드를 스택에 넣습니다.
- **핵심**: 왼쪽 끝까지 도달해야 중위 순회의 첫 번째 노드를 찾을 수 있습니다.

```python
    current = stack.pop()
    result.append(current.val)
    current = current.right
```
- 스택에서 꺼낸 노드가 현재 방문할 노드입니다.
- 값을 결과에 추가한 후 오른쪽 자식으로 이동합니다.

### 실행 예제

```
트리:     4
        / \
       2   6

스택: []     current=4  → 스택에 4 추가, 왼쪽으로
스택: [4]    current=2  → 스택에 2 추가, 왼쪽으로
스택: [4,2]  current=None → pop: 2, result=[2], 오른쪽=None
스택: [4]    current=None → pop: 4, result=[2,4], 오른쪽=6
스택: []     current=6  → 스택에 6 추가, 왼쪽=None
스택: [6]    current=None → pop: 6, result=[2,4,6]

결과: [2, 4, 6]
```

---

## 접근법 3: Morris Traversal (공간 O(1))

추가 공간(스택/재귀) 없이 중위 순회를 수행합니다. 스레드(thread)를 이용하여 트리 구조를 일시적으로 변경합니다.

```python
def inorder_morris(root: TreeNode) -> list:
```

### 라인별 설명

```python
if not current.left:
    result.append(current.val)
    current = current.right
```
- 왼쪽 자식이 없으면 바로 방문하고 오른쪽으로 이동합니다.

```python
predecessor = current.left
while predecessor.right and predecessor.right != current:
    predecessor = predecessor.right
```
- 왼쪽 서브트리에서 **중위 순회 전임자(predecessor)**를 찾습니다.
- 전임자는 왼쪽 서브트리의 가장 오른쪽 노드입니다.

```python
if not predecessor.right:
    predecessor.right = current
    current = current.left
else:
    predecessor.right = None
    result.append(current.val)
    current = current.right
```
- **스레드 생성**: 전임자의 오른쪽을 현재 노드로 연결하고 왼쪽으로 이동합니다.
- **스레드 제거**: 이미 스레드가 있으면 제거하고 현재 노드를 방문합니다.
- 트리 구조를 원래대로 복원하므로 트리가 변하지 않습니다.

### 실행 예제

```
트리:     4
        / \
       2   6
      / \
     1   3

1. current=4, predecessor=3 → 3.right=4(스레드), current=2
2. current=2, predecessor=1 → 1.right=2(스레드), current=1
3. current=1, 왼쪽 없음 → result=[1], current=2(스레드)
4. current=2, predecessor=1, 1.right==2 → 스레드 제거, result=[1,2], current=3
5. current=3, 왼쪽 없음 → result=[1,2,3], current=4(스레드)
6. current=4, predecessor=3, 3.right==4 → 스레드 제거, result=[1,2,3,4], current=6
7. current=6, 왼쪽 없음 → result=[1,2,3,4,6]

결과: [1, 2, 3, 4, 6]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 재귀 | O(N) | O(H) 호출 스택 |
| 반복 (스택) | O(N) | O(H) 스택 |
| Morris | O(N) | O(1) |

- N: 노드 수, H: 트리 높이
- BST에서 중위 순회는 노드를 **오름차순**으로 방문합니다.
- Morris Traversal은 공간 효율이 뛰어나지만 트리를 일시적으로 변경합니다.
