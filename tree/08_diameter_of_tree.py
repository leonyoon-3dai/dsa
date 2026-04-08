"""
Tree Algorithm Example 8: Diameter of Binary Tree (이진 트리 지름)
이진 트리의 지름(가장 먼 두 노드 사이의 경로 길이)을 구하는 알고리즘

Problem: 이진 트리의 지름을 구하라. 지름은 임의의 두 노드 사이의 최장 경로의 간선 수이다.
이 경로는 루트를 지나지 않을 수도 있다.
"""


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def diameter_global_variable(root: TreeNode) -> int:
    """접근법 1: 전역 변수를 이용한 DFS"""
    # 지름을 저장할 리스트 (클로저 대용)
    diameter = [0]

    # 각 노드에서 높이를 계산하며 지름을 갱신하는 함수
    def height(node: TreeNode) -> int:
        # 노드가 None이면 높이 0
        if not node:
            return 0

        # 왼쪽 서브트리의 높이를 구함
        left_h = height(node.left)
        # 오른쪽 서브트리의 높이를 구함
        right_h = height(node.right)

        # 현재 노드를 지나는 경로 = 왼쪽 높이 + 오른쪽 높이
        diameter[0] = max(diameter[0], left_h + right_h)

        # 현재 노드의 높이를 반환
        return max(left_h, right_h) + 1

    # 루트부터 높이 계산 시작
    height(root)
    # 지름 반환
    return diameter[0]


def diameter_return_tuple(root: TreeNode) -> int:
    """접근법 2: 튜플 반환 DFS"""

    # (높이, 지름)을 반환하는 헬퍼 함수
    def dfs(node: TreeNode) -> tuple:
        # 노드가 None이면 (높이 0, 지름 0)
        if not node:
            return (0, 0)

        # 왼쪽 서브트리의 (높이, 지름)
        left_h, left_d = dfs(node.left)
        # 오른쪽 서브트리의 (높이, 지름)
        right_h, right_d = dfs(node.right)

        # 현재 노드의 높이
        current_h = max(left_h, right_h) + 1
        # 현재 노드를 지나는 경로 길이
        through_current = left_h + right_h
        # 현재까지의 최대 지름
        current_d = max(left_d, right_d, through_current)

        # (높이, 지름) 튜플 반환
        return (current_h, current_d)

    # 루트부터 DFS 실행
    _, result = dfs(root)
    # 지름 반환
    return result


def diameter_bottom_up(root: TreeNode) -> int:
    """접근법 3: 스택을 이용한 반복적 후위 순회"""
    # 루트가 없으면 0 반환
    if not root:
        return 0

    # 각 노드의 높이를 저장할 딕셔너리
    heights = {}
    # 지름을 추적할 변수
    diameter = 0
    # 후위 순회를 위한 스택
    stack = [(root, False)]

    # 스택이 빌 때까지 반복
    while stack:
        # 노드와 방문 여부를 꺼냄
        node, visited = stack.pop()

        if visited:
            # 이미 자식을 처리한 노드: 높이 계산
            # 왼쪽 높이를 가져옴 (없으면 0)
            left_h = heights.get(id(node.left), 0) if node.left else 0
            # 오른쪽 높이를 가져옴 (없으면 0)
            right_h = heights.get(id(node.right), 0) if node.right else 0

            # 현재 노드의 높이를 저장
            heights[id(node)] = max(left_h, right_h) + 1
            # 현재 노드를 지나는 경로로 지름 갱신
            diameter = max(diameter, left_h + right_h)
        else:
            # 아직 자식을 처리하지 않은 노드
            # 현재 노드를 다시 스택에 넣음 (방문 표시)
            stack.append((node, True))
            # 오른쪽 자식을 먼저 스택에 넣음
            if node.right:
                stack.append((node.right, False))
            # 왼쪽 자식을 나중에 넣음
            if node.left:
                stack.append((node.left, False))

    # 지름 반환
    return diameter


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

    print("=== Diameter of Binary Tree (이진 트리 지름) ===")
    print(f"전역 변수: {diameter_global_variable(root)}")
    print(f"튜플 반환: {diameter_return_tuple(root)}")
    print(f"반복적: {diameter_bottom_up(root)}")

    # 루트를 지나지 않는 지름 예제:
    #         1
    #        /
    #       2
    #      / \
    #     3   4
    #    /     \
    #   5       6
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3, TreeNode(5), None)
    root2.left.right = TreeNode(4, None, TreeNode(6))

    print(f"\n루트를 지나지 않는 예제: {diameter_global_variable(root2)}")
