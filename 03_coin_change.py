"""
Dynamic Programming Example 3: Coin Change (동전 거스름돈)

Problem: 동전의 종류가 주어질 때, 금액 amount를 만드는 최소 동전 개수를 구하라.
         만들 수 없으면 -1을 반환.
LeetCode #322
"""


def coin_change(coins: list, amount: int) -> int:
    # dp[i] = 금액 i를 만드는 데 필요한 최소 동전 개수
    # amount + 1은 불가능한 값 (최대 amount개의 1원 동전이면 충분하므로)
    dp = [amount + 1] * (amount + 1)

    # 금액 0을 만드는 데 필요한 동전 수는 0개
    dp[0] = 0

    # 금액 1부터 amount까지 순회
    for i in range(1, amount + 1):
        # 각 동전 종류에 대해 확인
        for coin in coins:
            # 현재 금액 i에서 동전 값을 뺀 값이 0 이상이어야 사용 가능
            if coin <= i:
                # dp[i - coin] + 1 (해당 동전 1개 사용)과 현재 dp[i] 중 최솟값
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # dp[amount]가 초기값이면 만들 수 없으므로 -1 반환
    return dp[amount] if dp[amount] <= amount else -1


# === 실행 예제 ===
if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = 37
    result = coin_change(coins, amount)
    print(f"동전 종류: {coins}")
    print(f"금액 {amount}원을 만드는 최소 동전 수: {result}개")
