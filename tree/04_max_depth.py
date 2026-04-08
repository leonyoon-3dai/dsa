"""
Tree Algorithm Example 4: Maximum Depth of Binary Tree (최대 깊이)
이진 트리의 최대 깊이(높이)를 구하는 알고리즘

Problem: 이진 트리가 주어졌을 때, 루트에서 가장 먼 리프 노드까지의 경로 길이(깊이)를 구하라.
"""

from collections import deque


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_recursive(root: TreeNode) -> int:
    """접근법 1: 재귀적 DFS"""
    # 노드가 None이면 깊이 0
    if not root:
        return 0

    # 왼쪽 서브트리의 최대 깊이를 구함
    left_depth = max_depth_recursive(root.left)
    # 오른쪽 서브트리의 최대 깊이를 구함
    right_depth = max_depth_recursive(root.right)

    # 왼쪽과 오른쪽 중 더 깊은 쪽 + 1 (현재 노드)
    return max(left_depth, right_depth) + 1


def max_depth_iterative_bfs(root: TreeNode) -> int:
    """접근법 2: BFS (레벨 순회)"""
    # 루트가 없으면 깊이 0
    if not root:
        return 0

    # 깊이 카운터 초기화
    depth = 0
    # BFS 큐에 루트 노드를 넣음
    queue = deque([root])

    # 큐가 빌 때까지 반복
    while queue:
        # 현재 레벨의 노드 수를 저장
        level_size = len(queue)
        # 깊이 증가
        depth += 1

        # 현재 레벨의 모든 노드를 처리
        for _ in range(level_size):
            # 큐에서 노드를 꺼냄
            node = queue.popleft()

            # 왼쪽 자식이 있으면 큐에 추가
            if node.left:
                queue.append(node.left)
            # 오른쪽 자식이 있으면 큐에 추가
            if node.right:
                queue.append(node.right)

    # 최대 깊이 반환
    return depth


def max_depth_iterative_dfs(root: TreeNode) -> int:
    """접근법 3: 반복적 DFS (스택 사용)"""
    # 루트가 없으면 깊이 0
    if not root:
        return 0

    # 최대 깊이를 추적할 변수
    max_d = 0
    # 스택에 (노드, 현재 깊이) 쌍을 저장
    stack = [(root, 1)]

    # 스택이 빌 때까지 반복
    while stack:
        # 노드와 깊이를 꺼냄
        node, depth = stack.pop()

        # 현재 깊이와 최대 깊이를 비교하여 갱신
        max_d = max(max_d, depth)

        # 왼쪽 자식이 있으면 스택에 추가 (깊이 + 1)
        if node.left:
            stack.append((node.left, depth + 1))
        # 오른쪽 자식이 있으면 스택에 추가 (깊이 + 1)
        if node.right:
            stack.append((node.right, depth + 1))

    # 최대 깊이 반환
    return max_d


# === 실행 예제 ===
if __name__ == "__main__":
    # 트리 구성:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print("=== Maximum Depth (최대 깊이) ===")
    print(f"재귀 DFS: {max_depth_recursive(root)}")
    print(f"BFS: {max_depth_iterative_bfs(root)}")
    print(f"반복 DFS: {max_depth_iterative_dfs(root)}")

    # 한 쪽으로 치우친 트리
    #   1
    #    \
    #     2
    #      \
    #       3
    skewed = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(f"\n치우친 트리 깊이: {max_depth_recursive(skewed)}")

    # 빈 트리
    print(f"빈 트리 깊이: {max_depth_recursive(None)}")
