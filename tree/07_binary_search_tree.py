"""
Tree Algorithm Example 7: BST Insert/Search/Delete (이진 탐색 트리 연산)
이진 탐색 트리의 삽입, 검색, 삭제 연산 구현

Problem: 이진 탐색 트리에서 노드를 삽입, 검색, 삭제하는 함수를 구현하라.
"""


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def bst_search_recursive(root: TreeNode, target: int) -> TreeNode:
    """접근법 1: 재귀적 BST 검색"""
    # 노드가 없거나 현재 노드가 목표값이면 반환
    if not root or root.val == target:
        return root

    # 목표값이 현재 노드보다 작으면 왼쪽으로 탐색
    if target < root.val:
        return bst_search_recursive(root.left, target)

    # 목표값이 현재 노드보다 크면 오른쪽으로 탐색
    return bst_search_recursive(root.right, target)


def bst_search_iterative(root: TreeNode, target: int) -> TreeNode:
    """접근법 2: 반복적 BST 검색"""
    # 현재 노드를 루트로 설정
    current = root

    # 노드가 있는 동안 반복
    while current:
        # 목표값을 찾으면 반환
        if current.val == target:
            return current
        # 목표값이 작으면 왼쪽으로 이동
        elif target < current.val:
            current = current.left
        # 목표값이 크면 오른쪽으로 이동
        else:
            current = current.right

    # 못 찾으면 None 반환
    return None


def bst_insert(root: TreeNode, val: int) -> TreeNode:
    """BST 삽입 (재귀)"""
    # 빈 위치에 도달하면 새 노드 생성
    if not root:
        return TreeNode(val)

    # 삽입할 값이 현재 노드보다 작으면 왼쪽에 삽입
    if val < root.val:
        root.left = bst_insert(root.left, val)
    # 삽입할 값이 현재 노드보다 크면 오른쪽에 삽입
    elif val > root.val:
        root.right = bst_insert(root.right, val)

    # 같은 값은 삽입하지 않음 (중복 방지)
    # 현재 노드를 반환
    return root


def bst_delete(root: TreeNode, val: int) -> TreeNode:
    """BST 삭제"""
    # 노드가 없으면 반환
    if not root:
        return None

    # 삭제할 값이 현재 노드보다 작으면 왼쪽에서 삭제
    if val < root.val:
        root.left = bst_delete(root.left, val)
    # 삭제할 값이 현재 노드보다 크면 오른쪽에서 삭제
    elif val > root.val:
        root.right = bst_delete(root.right, val)
    else:
        # 삭제할 노드를 찾음

        # 경우 1: 자식이 없거나 하나만 있는 경우
        if not root.left:
            # 오른쪽 자식(또는 None)을 반환
            return root.right
        if not root.right:
            # 왼쪽 자식을 반환
            return root.left

        # 경우 2: 자식이 두 개인 경우
        # 오른쪽 서브트리에서 최솟값(후계자)을 찾음
        successor = root.right
        while successor.left:
            successor = successor.left

        # 현재 노드의 값을 후계자의 값으로 대체
        root.val = successor.val
        # 후계자를 오른쪽 서브트리에서 삭제
        root.right = bst_delete(root.right, successor.val)

    # 현재 노드를 반환
    return root


def inorder(root: TreeNode) -> list:
    """중위 순회로 BST의 값을 정렬된 순서로 반환"""
    # 노드가 없으면 빈 리스트
    if not root:
        return []
    # 왼쪽 + 현재 + 오른쪽
    return inorder(root.left) + [root.val] + inorder(root.right)


# === 실행 예제 ===
if __name__ == "__main__":
    # BST 구성
    root = None
    # 값들을 순서대로 삽입
    for val in [5, 3, 7, 1, 4, 6, 8]:
        root = bst_insert(root, val)

    print("=== BST Operations (BST 연산) ===")
    print(f"중위 순회: {inorder(root)}")

    # 검색
    print(f"\n=== 검색 ===")
    node = bst_search_recursive(root, 4)
    print(f"4 검색 (재귀): {'찾음' if node else '없음'}")
    node = bst_search_iterative(root, 9)
    print(f"9 검색 (반복): {'찾음' if node else '없음'}")

    # 삽입
    print(f"\n=== 삽입 ===")
    root = bst_insert(root, 2)
    print(f"2 삽입 후: {inorder(root)}")

    # 삭제
    print(f"\n=== 삭제 ===")
    root = bst_delete(root, 3)
    print(f"3 삭제 후: {inorder(root)}")
    root = bst_delete(root, 5)
    print(f"5 삭제 후: {inorder(root)}")
