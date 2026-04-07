"""
Dynamic Programming Example 9: Maximum Subarray (최대 부분 배열 합)

Problem: 정수 배열이 주어질 때, 합이 최대인 연속 부분 배열을 찾고 그 합을 반환하라.
         (Kadane's Algorithm)
LeetCode #53
"""


def max_subarray(nums: list) -> int:
    # 현재 위치에서 끝나는 부분 배열의 최대 합
    current_sum = nums[0]

    # 전체 최대 합 (첫 번째 원소로 초기화)
    max_sum = nums[0]

    # 두 번째 원소부터 순회
    for i in range(1, len(nums)):
        # 현재 원소를 기존 부분 배열에 이어붙이거나, 새로 시작하거나
        # max(이어붙이기, 새로시작) 중 큰 값 선택
        current_sum = max(nums[i], current_sum + nums[i])

        # 전체 최대 합 갱신
        max_sum = max(max_sum, current_sum)

    # 전체 최대 합 반환
    return max_sum


# === 실행 예제 ===
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"배열: {nums}")
    print(f"최대 부분 배열 합: {max_subarray(nums)}")  # 출력: 6 ([4,-1,2,1])

    nums2 = [5, 4, -1, 7, 8]
    print(f"\n배열: {nums2}")
    print(f"최대 부분 배열 합: {max_subarray(nums2)}")  # 출력: 23
