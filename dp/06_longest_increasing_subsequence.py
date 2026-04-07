"""
Dynamic Programming Example 6: Longest Increasing Subsequence (최장 증가 부분 수열)

Problem: 정수 배열이 주어질 때, 가장 긴 순증가 부분 수열의 길이를 구하라.
LeetCode #300
"""


def lis(nums: list) -> int:
    # 배열이 비어있으면 0 반환
    if not nums:
        return 0

    # 배열 길이
    n = len(nums)

    # dp[i] = nums[i]를 마지막 원소로 하는 LIS의 길이
    # 모든 원소는 자기 자신만으로 길이 1의 수열을 만들 수 있으므로 1로 초기화
    dp = [1] * n

    # 각 원소에 대해 (1번 인덱스부터)
    for i in range(1, n):
        # i 이전의 모든 원소를 확인
        for j in range(i):
            # nums[j] < nums[i]이면 증가하는 관계
            if nums[j] < nums[i]:
                # dp[i]를 dp[j]+1과 비교하여 더 큰 값으로 갱신
                dp[i] = max(dp[i], dp[j] + 1)

    # dp 배열에서 최댓값이 전체 LIS 길이
    return max(dp)


# === 실행 예제 ===
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"배열: {nums}")
    print(f"LIS 길이: {lis(nums)}")  # 출력: 4 ([2, 3, 7, 101])

    nums2 = [0, 1, 0, 3, 2, 3]
    print(f"\n배열: {nums2}")
    print(f"LIS 길이: {lis(nums2)}")  # 출력: 4 ([0, 1, 2, 3])
