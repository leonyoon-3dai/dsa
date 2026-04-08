"""
Tree Algorithm Example 5: Validate BST (이진 탐색 트리 검증)
주어진 이진 트리가 유효한 이진 탐색 트리(BST)인지 확인

Problem: 이진 트리가 주어졌을 때, 모든 노드가 BST 속성을 만족하는지 검증하라.
BST 속성: 왼쪽 서브트리의 모든 값 < 현재 노드 값 < 오른쪽 서브트리의 모든 값
"""

import math


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst_recursive(root: TreeNode) -> bool:
    """접근법 1: 재귀적 범위 검증"""

    # 노드의 값이 유효한 범위 내에 있는지 확인하는 헬퍼 함수
    def validate(node: TreeNode, low: float, high: float) -> bool:
        # 노드가 None이면 유효함
        if not node:
            return True

        # 현재 노드의 값이 허용 범위를 벗어나면 유효하지 않음
        if node.val <= low or node.val >= high:
            return False

        # 왼쪽 서브트리: 상한을 현재 값으로 업데이트
        left_valid = validate(node.left, low, node.val)
        # 오른쪽 서브트리: 하한을 현재 값으로 업데이트
        right_valid = validate(node.right, node.val, high)

        # 양쪽 모두 유효해야 전체가 유효
        return left_valid and right_valid

    # 초기 범위: 음의 무한대 ~ 양의 무한대
    return validate(root, -math.inf, math.inf)


def is_valid_bst_inorder(root: TreeNode) -> bool:
    """접근법 2: 중위 순회를 이용한 검증"""
    # 이전에 방문한 노드의 값을 저장할 리스트 (클로저용)
    prev = [-math.inf]

    # 중위 순회 헬퍼 함수
    def inorder(node: TreeNode) -> bool:
        # 노드가 None이면 유효함
        if not node:
            return True

        # 왼쪽 서브트리가 유효하지 않으면 False
        if not inorder(node.left):
            return False

        # 중위 순회에서 값이 오름차순이어야 함
        if node.val <= prev[0]:
            return False

        # 이전 값을 현재 값으로 업데이트
        prev[0] = node.val

        # 오른쪽 서브트리 검증
        return inorder(node.right)

    # 루트부터 검증 시작
    return inorder(root)


def is_valid_bst_iterative(root: TreeNode) -> bool:
    """접근법 3: 반복적 중위 순회"""
    # 스택 초기화
    stack = []
    # 현재 노드를 루트로 설정
    current = root
    # 이전 값 초기화
    prev = -math.inf

    # 현재 노드가 있거나 스택이 비어있지 않으면 계속
    while current or stack:
        # 왼쪽 끝까지 이동
        while current:
            # 현재 노드를 스택에 추가
            stack.append(current)
            # 왼쪽으로 이동
            current = current.left

        # 스택에서 노드를 꺼냄
        current = stack.pop()

        # 이전 값보다 크지 않으면 유효하지 않음
        if current.val <= prev:
            return False

        # 이전 값을 현재 값으로 업데이트
        prev = current.val
        # 오른쪽 자식으로 이동
        current = current.right

    # 모든 노드가 유효하면 True
    return True


# === 실행 예제 ===
if __name__ == "__main__":
    # 유효한 BST:
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   1  4 6  8
    valid_bst = TreeNode(5)
    valid_bst.left = TreeNode(3, TreeNode(1), TreeNode(4))
    valid_bst.right = TreeNode(7, TreeNode(6), TreeNode(8))

    print("=== Validate BST (BST 검증) ===")
    print(f"유효한 BST (재귀): {is_valid_bst_recursive(valid_bst)}")
    print(f"유효한 BST (중위): {is_valid_bst_inorder(valid_bst)}")
    print(f"유효한 BST (반복): {is_valid_bst_iterative(valid_bst)}")

    # 유효하지 않은 BST:
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    invalid_bst = TreeNode(5)
    invalid_bst.left = TreeNode(1)
    invalid_bst.right = TreeNode(4, TreeNode(3), TreeNode(6))

    print(f"\n유효하지 않은 BST (재귀): {is_valid_bst_recursive(invalid_bst)}")
    print(f"유효하지 않은 BST (중위): {is_valid_bst_inorder(invalid_bst)}")
    print(f"유효하지 않은 BST (반복): {is_valid_bst_iterative(invalid_bst)}")
