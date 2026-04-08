"""
Tree Algorithm Example 2: Preorder & Postorder Traversal (전위/후위 순회)
전위 순회: 루트 → 왼쪽 → 오른쪽 / 후위 순회: 왼쪽 → 오른쪽 → 루트

Problem: 주어진 이진 트리를 전위 순회와 후위 순회하여 노드 값을 순서대로 반환하라.
"""


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def preorder_recursive(root: TreeNode) -> list:
    """접근법 1: 재귀적 전위 순회"""
    # 결과를 저장할 리스트
    result = []

    # 내부 헬퍼 함수
    def helper(node: TreeNode) -> None:
        # 노드가 None이면 반환
        if not node:
            return
        # 현재 노드를 먼저 방문 (전위)
        result.append(node.val)
        # 왼쪽 서브트리 순회
        helper(node.left)
        # 오른쪽 서브트리 순회
        helper(node.right)

    # 루트부터 순회 시작
    helper(root)
    # 결과 반환
    return result


def preorder_iterative(root: TreeNode) -> list:
    """접근법 2: 반복적 전위 순회 (스택 사용)"""
    # 루트가 없으면 빈 리스트 반환
    if not root:
        return []

    # 결과를 저장할 리스트
    result = []
    # 스택에 루트 노드를 넣음
    stack = [root]

    # 스택이 빌 때까지 반복
    while stack:
        # 스택에서 노드를 꺼냄
        node = stack.pop()
        # 꺼낸 노드의 값을 결과에 추가
        result.append(node.val)

        # 오른쪽 자식을 먼저 스택에 넣음 (나중에 처리되도록)
        if node.right:
            stack.append(node.right)
        # 왼쪽 자식을 나중에 넣음 (먼저 처리되도록)
        if node.left:
            stack.append(node.left)

    # 결과 반환
    return result


def postorder_recursive(root: TreeNode) -> list:
    """접근법 3: 재귀적 후위 순회"""
    # 결과를 저장할 리스트
    result = []

    # 내부 헬퍼 함수
    def helper(node: TreeNode) -> None:
        # 노드가 None이면 반환
        if not node:
            return
        # 왼쪽 서브트리를 먼저 순회
        helper(node.left)
        # 오른쪽 서브트리를 순회
        helper(node.right)
        # 현재 노드를 마지막에 방문 (후위)
        result.append(node.val)

    # 루트부터 순회 시작
    helper(root)
    # 결과 반환
    return result


def postorder_iterative(root: TreeNode) -> list:
    """접근법 4: 반복적 후위 순회 (두 개의 스택)"""
    # 루트가 없으면 빈 리스트 반환
    if not root:
        return []

    # 첫 번째 스택: 탐색용
    stack1 = [root]
    # 두 번째 스택: 결과 역순 저장용
    stack2 = []

    # 첫 번째 스택이 빌 때까지 반복
    while stack1:
        # 노드를 꺼내서 두 번째 스택에 추가
        node = stack1.pop()
        stack2.append(node)

        # 왼쪽 자식을 먼저 첫 번째 스택에 추가
        if node.left:
            stack1.append(node.left)
        # 오른쪽 자식을 나중에 첫 번째 스택에 추가
        if node.right:
            stack1.append(node.right)

    # 두 번째 스택을 역순으로 꺼내면 후위 순회 결과
    result = []
    while stack2:
        result.append(stack2.pop().val)

    # 결과 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 트리 구성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)

    print("=== Preorder Traversal (전위 순회) ===")
    print(f"재귀: {preorder_recursive(root)}")
    print(f"반복: {preorder_iterative(root)}")

    print("\n=== Postorder Traversal (후위 순회) ===")
    print(f"재귀: {postorder_recursive(root)}")
    print(f"반복: {postorder_iterative(root)}")
