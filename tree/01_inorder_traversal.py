"""
Tree Algorithm Example 1: Inorder Traversal (중위 순회)
이진 트리의 중위 순회 - 왼쪽 → 루트 → 오른쪽 순서로 노드를 방문

Problem: 주어진 이진 트리를 중위 순회하여 노드 값을 순서대로 반환하라.
"""


class TreeNode:
    # 이진 트리의 노드를 나타내는 클래스
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        # 노드의 값
        self.val = val
        # 왼쪽 자식 노드
        self.left = left
        # 오른쪽 자식 노드
        self.right = right


def inorder_recursive(root: TreeNode) -> list:
    """접근법 1: 재귀적 중위 순회"""
    # 결과를 저장할 리스트
    result = []

    # 내부 헬퍼 함수 정의
    def helper(node: TreeNode) -> None:
        # 노드가 None이면 반환 (기저 조건)
        if not node:
            return
        # 왼쪽 서브트리를 먼저 순회
        helper(node.left)
        # 현재 노드의 값을 결과에 추가
        result.append(node.val)
        # 오른쪽 서브트리를 순회
        helper(node.right)

    # 루트부터 순회 시작
    helper(root)
    # 결과 반환
    return result


def inorder_iterative(root: TreeNode) -> list:
    """접근법 2: 반복적 중위 순회 (스택 사용)"""
    # 결과를 저장할 리스트
    result = []
    # 스택 초기화
    stack = []
    # 현재 노드를 루트로 설정
    current = root

    # 현재 노드가 있거나 스택에 노드가 남아있으면 계속
    while current or stack:
        # 왼쪽 끝까지 이동하며 스택에 푸시
        while current:
            # 현재 노드를 스택에 추가
            stack.append(current)
            # 왼쪽 자식으로 이동
            current = current.left

        # 스택에서 노드를 꺼냄
        current = stack.pop()
        # 꺼낸 노드의 값을 결과에 추가
        result.append(current.val)
        # 오른쪽 자식으로 이동
        current = current.right

    # 결과 반환
    return result


def inorder_morris(root: TreeNode) -> list:
    """접근법 3: Morris Traversal (공간 O(1) 중위 순회)"""
    # 결과를 저장할 리스트
    result = []
    # 현재 노드를 루트로 설정
    current = root

    # 현재 노드가 있으면 계속
    while current:
        # 왼쪽 자식이 없으면 현재 노드를 방문하고 오른쪽으로 이동
        if not current.left:
            # 현재 노드의 값을 결과에 추가
            result.append(current.val)
            # 오른쪽 자식으로 이동
            current = current.right
        else:
            # 왼쪽 서브트리에서 현재 노드의 전임자(predecessor) 찾기
            predecessor = current.left
            # 오른쪽 끝까지 이동 (현재 노드로의 링크 제외)
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            # 전임자의 오른쪽이 비어있으면 스레드 연결
            if not predecessor.right:
                # 현재 노드로의 스레드 생성
                predecessor.right = current
                # 왼쪽으로 이동
                current = current.left
            else:
                # 스레드가 이미 있으면 제거하고 노드 방문
                predecessor.right = None
                # 현재 노드의 값을 결과에 추가
                result.append(current.val)
                # 오른쪽으로 이동
                current = current.right

    # 결과 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 트리 구성:
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(6, TreeNode(5), TreeNode(7))

    print("=== Inorder Traversal (중위 순회) ===")
    print(f"재귀: {inorder_recursive(root)}")
    print(f"반복: {inorder_iterative(root)}")
    print(f"Morris: {inorder_morris(root)}")

    # 빈 트리 테스트
    print("\n=== 빈 트리 ===")
    print(f"재귀: {inorder_recursive(None)}")
    print(f"반복: {inorder_iterative(None)}")
    print(f"Morris: {inorder_morris(None)}")
