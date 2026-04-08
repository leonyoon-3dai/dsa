"""
Greedy Example 6: Jump Game (점프 게임)

Problem: 정수 배열 nums가 주어지고, 각 원소는 해당 위치에서 점프할 수 있는 최대 거리이다.
         인덱스 0에서 시작하여 마지막 인덱스에 도달할 수 있는지 판별하라.
LeetCode #55
"""


def can_jump_greedy(nums: list[int]) -> bool:
    # 현재까지 도달할 수 있는 가장 먼 인덱스
    max_reach = 0

    # 배열을 순회
    for i in range(len(nums)):
        # 현재 인덱스가 도달 가능 범위를 벗어나면 불가능
        if i > max_reach:
            return False

        # 현재 위치에서 갈 수 있는 최대 인덱스로 max_reach 갱신
        max_reach = max(max_reach, i + nums[i])

        # 이미 마지막에 도달 가능하면 조기 종료
        if max_reach >= len(nums) - 1:
            return True

    # 모든 인덱스를 확인한 후 결과 반환
    return max_reach >= len(nums) - 1


def can_jump_backward(nums: list[int]) -> bool:
    # 역방향 그리디: 마지막부터 역추적
    n = len(nums)

    # 목표 위치를 마지막 인덱스로 설정
    goal = n - 1

    # 뒤에서 앞으로 순회
    for i in range(n - 2, -1, -1):
        # 현재 위치에서 목표에 도달할 수 있으면
        if i + nums[i] >= goal:
            # 목표를 현재 위치로 앞당김
            goal = i

    # 목표가 0이면 시작점에서 끝까지 도달 가능
    return goal == 0


def min_jumps_greedy(nums: list[int]) -> int:
    # Jump Game II: 최소 점프 횟수 (LeetCode #45)
    n = len(nums)

    # 배열 길이가 1이면 점프 불필요
    if n <= 1:
        return 0

    # 점프 횟수
    jumps = 0
    # 현재 점프로 도달 가능한 최대 범위
    current_end = 0
    # 다음 점프로 도달 가능한 최대 범위
    farthest = 0

    # 마지막 인덱스 전까지만 순회
    for i in range(n - 1):
        # 현재 위치에서 갈 수 있는 가장 먼 곳 갱신
        farthest = max(farthest, i + nums[i])

        # 현재 점프의 범위 끝에 도달하면
        if i == current_end:
            # 점프 횟수 증가
            jumps += 1
            # 다음 점프의 범위로 갱신
            current_end = farthest

            # 이미 마지막에 도달 가능하면 종료
            if current_end >= n - 1:
                break

    # 최소 점프 횟수 반환
    return jumps


# === 실행 예제 ===
if __name__ == "__main__":
    # 도달 가능한 경우
    nums1 = [2, 3, 1, 1, 4]
    print(f"배열: {nums1}")
    print(f"도달 가능 (정방향 그리디): {can_jump_greedy(nums1)}")
    print(f"도달 가능 (역방향 그리디): {can_jump_backward(nums1)}")
    print(f"최소 점프 횟수: {min_jumps_greedy(nums1)}")
    print()

    # 도달 불가능한 경우
    nums2 = [3, 2, 1, 0, 4]
    print(f"배열: {nums2}")
    print(f"도달 가능 (정방향 그리디): {can_jump_greedy(nums2)}")
    print(f"도달 가능 (역방향 그리디): {can_jump_backward(nums2)}")
    print()

    # 추가 예제
    nums3 = [1, 1, 1, 1, 1]
    print(f"배열: {nums3}")
    print(f"최소 점프 횟수: {min_jumps_greedy(nums3)}")
