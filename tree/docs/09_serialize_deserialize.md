# 09. Serialize & Deserialize Binary Tree (직렬화/역직렬화)

## 문제 정의

이진 트리를 문자열로 직렬화(serialize)하고, 해당 문자열로부터 원래 트리를 복원(deserialize)하라.
직렬화된 문자열은 트리의 구조와 값을 완전히 보존해야 한다.

---

## 접근법 1: 전위 순회 기반 직렬화/역직렬화

전위 순회로 트리를 문자열로 변환하고 복원합니다.

```python
def serialize_preorder(root: TreeNode) -> str:
def deserialize_preorder(data: str) -> TreeNode:
```

### 라인별 설명 (직렬화)

```python
def helper(node: TreeNode) -> None:
    if not node:
        result.append("null")
        return
    result.append(str(node.val))
    helper(node.left)
    helper(node.right)
```
- **핵심**: `None` 노드를 `"null"`로 표시하여 트리 구조를 보존합니다.
- 전위 순회: 루트 → 왼쪽 → 오른쪽 순서로 값을 기록합니다.
- `"null"` 마커가 없으면 트리 구조를 복원할 수 없습니다.

```python
return ",".join(result)
```
- 모든 값을 쉼표로 연결하여 하나의 문자열로 만듭니다.

### 라인별 설명 (역직렬화)

```python
tokens = deque(data.split(","))
```
- 문자열을 쉼표로 분리하여 큐에 넣습니다.
- **deque 사용 이유**: `popleft()`가 O(1)이므로 효율적입니다.

```python
def helper() -> TreeNode:
    val = tokens.popleft()
    if val == "null":
        return None
    node = TreeNode(int(val))
    node.left = helper()
    node.right = helper()
    return node
```
- **핵심**: 직렬화와 동일한 순서(전위)로 토큰을 소비합니다.
- `"null"`을 만나면 `None`을 반환하여 서브트리의 끝을 표시합니다.
- 재귀 호출 순서가 직렬화 순서와 일치하므로 정확히 복원됩니다.

### 실행 예제

```
트리:     1
        / \
       2   3
          / \
         4   5

직렬화: "1,2,null,null,3,4,null,null,5,null,null"

역직렬화:
  popleft() = "1" → 노드 1
    popleft() = "2" → 노드 2
      popleft() = "null" → None (왼쪽)
      popleft() = "null" → None (오른쪽)
    popleft() = "3" → 노드 3
      popleft() = "4" → 노드 4
        popleft() = "null" → None
        popleft() = "null" → None
      popleft() = "5" → 노드 5
        popleft() = "null" → None
        popleft() = "null" → None

복원된 트리: 원래와 동일
```

---

## 접근법 2: BFS(레벨 순회) 기반 직렬화/역직렬화

레벨별로 노드를 기록하고 복원합니다.

```python
def serialize_bfs(root: TreeNode) -> str:
def deserialize_bfs(data: str) -> TreeNode:
```

### 라인별 설명 (직렬화)

```python
queue = deque([root])
while queue:
    node = queue.popleft()
    if not node:
        result.append("null")
    else:
        result.append(str(node.val))
        queue.append(node.left)
        queue.append(node.right)
```
- BFS로 레벨별로 순회하며 값을 기록합니다.
- `None` 노드도 큐에 넣어 자리를 표시합니다.

```python
while result and result[-1] == "null":
    result.pop()
```
- 끝의 불필요한 `"null"`을 제거하여 문자열을 압축합니다.

### 라인별 설명 (역직렬화)

```python
root = TreeNode(int(tokens[0]))
queue = deque([root])
i = 1
```
- 첫 번째 토큰으로 루트를 생성하고 큐에 넣습니다.

```python
while queue and i < len(tokens):
    node = queue.popleft()
    if i < len(tokens) and tokens[i] != "null":
        node.left = TreeNode(int(tokens[i]))
        queue.append(node.left)
    i += 1
    if i < len(tokens) and tokens[i] != "null":
        node.right = TreeNode(int(tokens[i]))
        queue.append(node.right)
    i += 1
```
- 큐에서 부모 노드를 꺼내고, 다음 두 토큰이 왼쪽/오른쪽 자식입니다.
- **핵심**: 토큰 인덱스 `i`를 두 칸씩 증가시키며 자식 쌍을 처리합니다.

### 실행 예제

```
트리:     1
        / \
       2   3
          / \
         4   5

BFS 직렬화: "1,2,3,null,null,4,5"

역직렬화:
  tokens = ["1", "2", "3", "null", "null", "4", "5"]
  root = 1, queue = [1], i = 1
  pop 1: left = 2 (i=1), right = 3 (i=2), i = 3
  pop 2: left = null (i=3), right = null (i=4), i = 5
  pop 3: left = 4 (i=5), right = 5 (i=6), i = 7
```

---

## 접근법 3: 괄호 표기법

트리를 중첩된 괄호로 표현합니다.

```python
def serialize_parentheses(root: TreeNode) -> str:
```

### 라인별 설명

```python
if not root:
    return "()"
left = serialize_parentheses(root.left)
right = serialize_parentheses(root.right)
return f"({root.val}{left}{right})"
```
- 각 노드를 `(값(왼쪽)(오른쪽))` 형태로 표현합니다.
- 빈 노드는 `()`로 표시합니다.
- 사람이 읽기 쉽지만 역직렬화가 복잡합니다.

### 실행 예제

```
트리:     1
        / \
       2   3

결과: "(1(2()())(3()()))"
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 | 문자열 길이 |
|--------|------------|------------|------------|
| 전위 순회 | O(N) | O(N) | O(N) |
| BFS | O(N) | O(N) | O(N) (끝 null 제거) |
| 괄호 표기법 | O(N) | O(N) | O(N) |

- N: 노드 수
- 전위 순회 방식이 구현이 가장 간단하고 직관적입니다.
- BFS 방식은 LeetCode 등에서 트리를 표현하는 표준 형식입니다.
