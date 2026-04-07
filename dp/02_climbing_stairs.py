"""
Dynamic Programming Example 2: Climbing Stairs (계단 오르기)

Problem: 계단이 n개 있다. 한 번에 1칸 또는 2칸 오를 수 있을 때,
         꼭대기에 도달하는 방법의 수를 구하라.
LeetCode #70
"""


def climbing_stairs(n: int) -> int:
    # n이 1 이하이면 방법은 1가지뿐 (아무것도 안 하거나 1칸 오르기)
    if n <= 1:
        return 1

    # dp[i] = i번째 계단에 도달하는 방법의 수
    dp = [0] * (n + 1)

    # 0번째 계단(출발점)에 도달하는 방법: 1가지
    dp[0] = 1

    # 1번째 계단에 도달하는 방법: 1가지 (1칸 오르기)
    dp[1] = 1

    # 2번째 계단부터 n번째 계단까지 반복
    for i in range(2, n + 1):
        # i번째 계단에 도달하는 방법 =
        #   (i-1)번째에서 1칸 오르기 + (i-2)번째에서 2칸 오르기
        dp[i] = dp[i - 1] + dp[i - 2]

    # n번째 계단에 도달하는 방법의 수를 반환
    return dp[n]


# === 실행 예제 ===
if __name__ == "__main__":
    for n in range(1, 11):
        print(f"계단 {n}칸: {climbing_stairs(n)}가지 방법")
