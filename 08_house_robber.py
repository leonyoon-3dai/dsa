"""
Dynamic Programming Example 8: House Robber (도둑 문제)

Problem: 일렬로 늘어선 집들에 각각 돈이 있다.
         인접한 두 집을 연속으로 털 수 없을 때, 훔칠 수 있는 최대 금액을 구하라.
LeetCode #198
"""


def house_robber(nums: list) -> int:
    # 집이 없으면 0 반환
    if not nums:
        return 0

    # 집이 1개면 그 집의 금액 반환
    if len(nums) == 1:
        return nums[0]

    n = len(nums)

    # dp[i] = i번째 집까지 고려했을 때 훔칠 수 있는 최대 금액
    dp = [0] * n

    # 첫 번째 집만 있을 때: 그 집을 턴다
    dp[0] = nums[0]

    # 두 번째 집까지 있을 때: 둘 중 큰 금액을 선택
    dp[1] = max(nums[0], nums[1])

    # 세 번째 집부터 순회
    for i in range(2, n):
        # i번째 집을 터는 경우: dp[i-2] + nums[i] (i-1번째는 건너뜀)
        # i번째 집을 안 터는 경우: dp[i-1]
        # 둘 중 큰 값을 선택
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    # 마지막 집까지 고려한 최대 금액 반환
    return dp[n - 1]


# === 실행 예제 ===
if __name__ == "__main__":
    houses = [2, 7, 9, 3, 1]
    print(f"집별 금액: {houses}")
    print(f"최대 금액: {house_robber(houses)}")  # 출력: 12 (2+9+1)

    houses2 = [1, 2, 3, 1]
    print(f"\n집별 금액: {houses2}")
    print(f"최대 금액: {house_robber(houses2)}")  # 출력: 4 (1+3)
