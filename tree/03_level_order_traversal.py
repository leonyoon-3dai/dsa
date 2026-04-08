"""
Tree Algorithm Example 3: Level Order Traversal (레벨 순회)
이진 트리를 레벨별로 순회하여 각 레벨의 노드 값을 반환

Problem: 이진 트리가 주어졌을 때, 레벨별로 노드 값을 그룹화하여 반환하라.
"""

from collections import deque


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def level_order_bfs(root: TreeNode) -> list:
    """접근법 1: BFS를 이용한 레벨 순회"""
    # 루트가 없으면 빈 리스트 반환
    if not root:
        return []

    # 결과를 저장할 리스트
    result = []
    # BFS 큐에 루트 노드를 넣음
    queue = deque([root])

    # 큐가 빌 때까지 반복
    while queue:
        # 현재 레벨의 노드 수를 저장
        level_size = len(queue)
        # 현재 레벨의 값을 저장할 리스트
        level = []

        # 현재 레벨의 모든 노드를 처리
        for _ in range(level_size):
            # 큐에서 노드를 꺼냄
            node = queue.popleft()
            # 현재 레벨 리스트에 값 추가
            level.append(node.val)

            # 왼쪽 자식이 있으면 큐에 추가
            if node.left:
                queue.append(node.left)
            # 오른쪽 자식이 있으면 큐에 추가
            if node.right:
                queue.append(node.right)

        # 현재 레벨의 결과를 전체 결과에 추가
        result.append(level)

    # 결과 반환
    return result


def level_order_dfs(root: TreeNode) -> list:
    """접근법 2: DFS를 이용한 레벨 순회"""
    # 결과를 저장할 리스트
    result = []

    # DFS 헬퍼 함수
    def dfs(node: TreeNode, depth: int) -> None:
        # 노드가 없으면 반환
        if not node:
            return

        # 현재 깊이의 레벨 리스트가 없으면 생성
        if depth == len(result):
            result.append([])

        # 현재 깊이의 레벨에 값 추가
        result[depth].append(node.val)

        # 왼쪽 서브트리 탐색 (깊이 + 1)
        dfs(node.left, depth + 1)
        # 오른쪽 서브트리 탐색 (깊이 + 1)
        dfs(node.right, depth + 1)

    # 루트부터 깊이 0으로 시작
    dfs(root, 0)
    # 결과 반환
    return result


def zigzag_level_order(root: TreeNode) -> list:
    """접근법 3: 지그재그 레벨 순회"""
    # 루트가 없으면 빈 리스트 반환
    if not root:
        return []

    # 결과를 저장할 리스트
    result = []
    # BFS 큐에 루트 노드를 넣음
    queue = deque([root])
    # 왼쪽에서 오른쪽 방향 플래그
    left_to_right = True

    # 큐가 빌 때까지 반복
    while queue:
        # 현재 레벨의 노드 수
        level_size = len(queue)
        # 현재 레벨의 값을 저장할 deque
        level = deque()

        # 현재 레벨의 모든 노드를 처리
        for _ in range(level_size):
            # 큐에서 노드를 꺼냄
            node = queue.popleft()

            # 방향에 따라 삽입 위치 결정
            if left_to_right:
                # 왼→오: 오른쪽에 추가
                level.append(node.val)
            else:
                # 오→왼: 왼쪽에 추가
                level.appendleft(node.val)

            # 자식 노드를 큐에 추가
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # 현재 레벨을 결과에 추가
        result.append(list(level))
        # 방향 전환
        left_to_right = not left_to_right

    # 결과 반환
    return result


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

    print("=== Level Order Traversal (레벨 순회) ===")
    print(f"BFS: {level_order_bfs(root)}")
    print(f"DFS: {level_order_dfs(root)}")

    print("\n=== Zigzag Level Order (지그재그 순회) ===")
    print(f"결과: {zigzag_level_order(root)}")
