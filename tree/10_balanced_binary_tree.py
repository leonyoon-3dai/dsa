"""
Tree Algorithm Example 10: Balanced Binary Tree (균형 이진 트리)
이진 트리가 높이 균형(height-balanced)인지 확인하는 알고리즘

Problem: 이진 트리가 주어졌을 때, 모든 노드에서 왼쪽과 오른쪽 서브트리의
높이 차이가 1 이하인지 확인하라.
"""


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced_top_down(root: TreeNode) -> bool:
    """접근법 1: 탑다운 방식 (각 노드에서 높이를 계산)"""

    # 노드의 높이를 계산하는 함수
    def height(node: TreeNode) -> int:
        # 노드가 없으면 높이 0
        if not node:
            return 0
        # 왼쪽과 오른쪽 높이 중 큰 값 + 1
        return max(height(node.left), height(node.right)) + 1

    # 노드가 없으면 균형
    if not root:
        return True

    # 왼쪽과 오른쪽 서브트리의 높이 차이를 계산
    left_h = height(root.left)
    right_h = height(root.right)

    # 높이 차이가 1 이하이고 양쪽 서브트리도 균형인지 확인
    if abs(left_h - right_h) > 1:
        return False

    # 왼쪽 서브트리가 균형인지 재귀적으로 확인
    left_balanced = is_balanced_top_down(root.left)
    # 오른쪽 서브트리가 균형인지 재귀적으로 확인
    right_balanced = is_balanced_top_down(root.right)

    # 양쪽 모두 균형이면 True
    return left_balanced and right_balanced


def is_balanced_bottom_up(root: TreeNode) -> bool:
    """접근법 2: 바텀업 방식 (높이 계산과 균형 확인을 동시에)"""

    # 높이를 반환하되, 불균형이면 -1을 반환하는 함수
    def check(node: TreeNode) -> int:
        # 노드가 없으면 높이 0
        if not node:
            return 0

        # 왼쪽 서브트리의 높이를 확인
        left_h = check(node.left)
        # 왼쪽이 불균형이면 즉시 -1 전파
        if left_h == -1:
            return -1

        # 오른쪽 서브트리의 높이를 확인
        right_h = check(node.right)
        # 오른쪽이 불균형이면 즉시 -1 전파
        if right_h == -1:
            return -1

        # 현재 노드에서 높이 차이가 1을 초과하면 불균형
        if abs(left_h - right_h) > 1:
            return -1

        # 현재 노드의 높이를 반환
        return max(left_h, right_h) + 1

    # -1이 아니면 균형
    return check(root) != -1


def is_balanced_iterative(root: TreeNode) -> bool:
    """접근법 3: 반복적 후위 순회 (스택 사용)"""
    # 루트가 없으면 균형
    if not root:
        return True

    # 각 노드의 높이를 저장할 딕셔너리
    heights = {}
    # 후위 순회를 위한 스택
    stack = [(root, False)]

    # 스택이 빌 때까지 반복
    while stack:
        # 노드와 방문 여부를 꺼냄
        node, visited = stack.pop()

        if visited:
            # 자식 노드들의 높이를 가져옴
            left_h = heights.get(id(node.left), 0) if node.left else 0
            right_h = heights.get(id(node.right), 0) if node.right else 0

            # 높이 차이가 1을 초과하면 불균형
            if abs(left_h - right_h) > 1:
                return False

            # 현재 노드의 높이를 저장
            heights[id(node)] = max(left_h, right_h) + 1
        else:
            # 후위 순회: 현재 노드를 방문 표시 후 다시 스택에
            stack.append((node, True))
            # 오른쪽 자식을 먼저 (스택이므로 나중에 처리)
            if node.right:
                stack.append((node.right, False))
            # 왼쪽 자식을 나중에
            if node.left:
                stack.append((node.left, False))

    # 모든 노드가 균형이면 True
    return True


# === 실행 예제 ===
if __name__ == "__main__":
    # 균형 트리:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    balanced = TreeNode(3)
    balanced.left = TreeNode(9)
    balanced.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print("=== Balanced Binary Tree (균형 이진 트리) ===")
    print(f"균형 트리 (탑다운): {is_balanced_top_down(balanced)}")
    print(f"균형 트리 (바텀업): {is_balanced_bottom_up(balanced)}")
    print(f"균형 트리 (반복적): {is_balanced_iterative(balanced)}")

    # 불균형 트리:
    #       1
    #      / \
    #     2   2
    #    / \
    #   3   3
    #  / \
    # 4   4
    unbalanced = TreeNode(1)
    unbalanced.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
    unbalanced.right = TreeNode(2)

    print(f"\n불균형 트리 (탑다운): {is_balanced_top_down(unbalanced)}")
    print(f"불균형 트리 (바텀업): {is_balanced_bottom_up(unbalanced)}")
    print(f"불균형 트리 (반복적): {is_balanced_iterative(unbalanced)}")
