"""
Tree Algorithm Example 9: Serialize & Deserialize Binary Tree (직렬화/역직렬화)
이진 트리를 문자열로 변환하고 다시 복원하는 알고리즘

Problem: 이진 트리를 문자열로 직렬화하고, 해당 문자열로부터 원래 트리를 복원하라.
"""

from collections import deque


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def serialize_preorder(root: TreeNode) -> str:
    """접근법 1: 전위 순회 기반 직렬화"""
    # 결과를 저장할 리스트
    result = []

    # 전위 순회 헬퍼 함수
    def helper(node: TreeNode) -> None:
        # 노드가 None이면 "null"을 추가
        if not node:
            result.append("null")
            return
        # 현재 노드의 값을 문자열로 추가
        result.append(str(node.val))
        # 왼쪽 서브트리 직렬화
        helper(node.left)
        # 오른쪽 서브트리 직렬화
        helper(node.right)

    # 루트부터 직렬화 시작
    helper(root)
    # 쉼표로 연결하여 문자열 반환
    return ",".join(result)


def deserialize_preorder(data: str) -> TreeNode:
    """접근법 1: 전위 순회 기반 역직렬화"""
    # 문자열을 쉼표로 분리하여 큐에 넣음
    tokens = deque(data.split(","))

    # 역직렬화 헬퍼 함수
    def helper() -> TreeNode:
        # 큐에서 토큰을 꺼냄
        val = tokens.popleft()

        # "null"이면 None 반환
        if val == "null":
            return None

        # 노드 생성
        node = TreeNode(int(val))
        # 왼쪽 서브트리 복원
        node.left = helper()
        # 오른쪽 서브트리 복원
        node.right = helper()
        # 노드 반환
        return node

    # 역직렬화 시작
    return helper()


def serialize_bfs(root: TreeNode) -> str:
    """접근법 2: BFS(레벨 순회) 기반 직렬화"""
    # 루트가 없으면 빈 문자열 반환
    if not root:
        return "null"

    # 결과를 저장할 리스트
    result = []
    # BFS 큐에 루트를 넣음
    queue = deque([root])

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 꺼냄
        node = queue.popleft()

        # 노드가 None이면 "null" 추가
        if not node:
            result.append("null")
        else:
            # 노드의 값을 문자열로 추가
            result.append(str(node.val))
            # 왼쪽 자식을 큐에 추가 (None이어도 추가)
            queue.append(node.left)
            # 오른쪽 자식을 큐에 추가 (None이어도 추가)
            queue.append(node.right)

    # 끝의 불필요한 "null" 제거
    while result and result[-1] == "null":
        result.pop()

    # 쉼표로 연결하여 반환
    return ",".join(result)


def deserialize_bfs(data: str) -> TreeNode:
    """접근법 2: BFS(레벨 순회) 기반 역직렬화"""
    # 빈 문자열이거나 "null"이면 None 반환
    if not data or data == "null":
        return None

    # 문자열을 토큰으로 분리
    tokens = data.split(",")
    # 루트 노드 생성
    root = TreeNode(int(tokens[0]))
    # BFS 큐에 루트를 넣음
    queue = deque([root])
    # 토큰 인덱스 초기화
    i = 1

    # 큐가 빌 때까지 반복
    while queue and i < len(tokens):
        # 현재 노드를 꺼냄
        node = queue.popleft()

        # 왼쪽 자식 처리
        if i < len(tokens) and tokens[i] != "null":
            # 왼쪽 자식 노드 생성
            node.left = TreeNode(int(tokens[i]))
            # 큐에 추가
            queue.append(node.left)
        # 인덱스 증가
        i += 1

        # 오른쪽 자식 처리
        if i < len(tokens) and tokens[i] != "null":
            # 오른쪽 자식 노드 생성
            node.right = TreeNode(int(tokens[i]))
            # 큐에 추가
            queue.append(node.right)
        # 인덱스 증가
        i += 1

    # 루트 반환
    return root


def serialize_parentheses(root: TreeNode) -> str:
    """접근법 3: 괄호 표기법 직렬화"""
    # 노드가 없으면 빈 문자열
    if not root:
        return "()"

    # 왼쪽 서브트리 직렬화
    left = serialize_parentheses(root.left)
    # 오른쪽 서브트리 직렬화
    right = serialize_parentheses(root.right)

    # 현재 노드와 자식을 괄호로 감싸서 반환
    return f"({root.val}{left}{right})"


def inorder_list(root: TreeNode) -> list:
    """검증용 중위 순회"""
    if not root:
        return []
    return inorder_list(root.left) + [root.val] + inorder_list(root.right)


# === 실행 예제 ===
if __name__ == "__main__":
    # 트리 구성:
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3, TreeNode(4), TreeNode(5))

    print("=== Serialize & Deserialize (직렬화/역직렬화) ===")

    # 전위 순회 방식
    serialized = serialize_preorder(root)
    print(f"전위 직렬화: {serialized}")
    restored = deserialize_preorder(serialized)
    print(f"복원 후 중위 순회: {inorder_list(restored)}")

    # BFS 방식
    serialized = serialize_bfs(root)
    print(f"\nBFS 직렬화: {serialized}")
    restored = deserialize_bfs(serialized)
    print(f"복원 후 중위 순회: {inorder_list(restored)}")

    # 괄호 표기법
    print(f"\n괄호 표기법: {serialize_parentheses(root)}")
