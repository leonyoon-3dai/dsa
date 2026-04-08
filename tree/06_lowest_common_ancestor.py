"""
Tree Algorithm Example 6: Lowest Common Ancestor (최소 공통 조상)
두 노드의 최소 공통 조상(LCA)을 찾는 알고리즘

Problem: 이진 트리에서 두 노드 p와 q의 최소 공통 조상을 찾아라.
최소 공통 조상: p와 q를 모두 자손으로 가지는 가장 깊은(가장 아래의) 노드.
"""


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def lca_binary_tree(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """접근법 1: 재귀적 LCA (일반 이진 트리)"""
    # 노드가 None이거나 p 또는 q를 찾으면 반환
    if not root or root == p or root == q:
        return root

    # 왼쪽 서브트리에서 p 또는 q를 찾음
    left = lca_binary_tree(root.left, p, q)
    # 오른쪽 서브트리에서 p 또는 q를 찾음
    right = lca_binary_tree(root.right, p, q)

    # 양쪽 모두에서 찾으면 현재 노드가 LCA
    if left and right:
        return root

    # 한 쪽에서만 찾으면 그 쪽 결과를 반환
    return left if left else right


def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """접근법 2: BST에서의 LCA (BST 속성 활용)"""
    # 현재 노드를 루트로 설정
    current = root

    # 노드가 있는 동안 반복
    while current:
        # p와 q 모두 현재 노드보다 작으면 왼쪽으로 이동
        if p.val < current.val and q.val < current.val:
            current = current.left
        # p와 q 모두 현재 노드보다 크면 오른쪽으로 이동
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            # p와 q가 서로 다른 쪽에 있으면 현재 노드가 LCA
            return current

    # 도달할 수 없는 코드 (유효한 입력 가정)
    return None


def lca_with_parent(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """접근법 3: 경로를 이용한 LCA"""
    # 루트에서 특정 노드까지의 경로를 찾는 함수
    def find_path(root: TreeNode, target: TreeNode) -> list:
        # 루트가 없으면 빈 리스트 반환
        if not root:
            return []

        # 현재 노드가 목표 노드이면 경로 반환
        if root == target:
            return [root]

        # 왼쪽 서브트리에서 경로 탐색
        left_path = find_path(root.left, target)
        # 왼쪽에서 찾으면 현재 노드를 앞에 추가
        if left_path:
            return [root] + left_path

        # 오른쪽 서브트리에서 경로 탐색
        right_path = find_path(root.right, target)
        # 오른쪽에서 찾으면 현재 노드를 앞에 추가
        if right_path:
            return [root] + right_path

        # 양쪽 모두에서 못 찾으면 빈 리스트
        return []

    # p까지의 경로를 구함
    path_p = find_path(root, p)
    # q까지의 경로를 구함
    path_q = find_path(root, q)

    # 두 경로에서 마지막으로 일치하는 노드가 LCA
    lca = None
    # 두 경로의 공통 부분을 찾음
    for i in range(min(len(path_p), len(path_q))):
        # 경로가 같으면 LCA 후보 업데이트
        if path_p[i] == path_q[i]:
            lca = path_p[i]
        else:
            # 경로가 갈라지면 중단
            break

    # LCA 반환
    return lca


# === 실행 예제 ===
if __name__ == "__main__":
    # 트리 구성:
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1, TreeNode(0), TreeNode(8))
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2, TreeNode(7), TreeNode(4))

    # p = 5, q = 1 → LCA = 3
    p, q = root.left, root.right
    print("=== LCA (최소 공통 조상) ===")
    result = lca_binary_tree(root, p, q)
    print(f"노드 {p.val}와 {q.val}의 LCA: {result.val}")

    # p = 5, q = 4 → LCA = 5
    p, q = root.left, root.left.right.right
    result = lca_binary_tree(root, p, q)
    print(f"노드 {p.val}와 {q.val}의 LCA: {result.val}")

    # BST 예제
    #       6
    #      / \
    #     2   8
    #    / \ / \
    #   0  4 7  9
    bst = TreeNode(6)
    bst.left = TreeNode(2, TreeNode(0), TreeNode(4))
    bst.right = TreeNode(8, TreeNode(7), TreeNode(9))

    print("\n=== BST LCA ===")
    p, q = bst.left, bst.right
    result = lca_bst(bst, p, q)
    print(f"노드 {p.val}와 {q.val}의 LCA: {result.val}")

    p, q = bst.left, bst.left.right
    result = lca_bst(bst, p, q)
    print(f"노드 {p.val}와 {q.val}의 LCA: {result.val}")
