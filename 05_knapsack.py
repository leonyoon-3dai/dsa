"""
Dynamic Programming Example 5: 0/1 Knapsack (배낭 문제)

Problem: n개의 물건이 있고 각각 무게와 가치가 있다.
         배낭의 용량 W가 주어질 때, 가치의 합이 최대가 되도록 물건을 선택하라.
         각 물건은 한 번만 선택 가능.
"""


def knapsack(weights: list, values: list, capacity: int) -> int:
    # 물건의 개수
    n = len(weights)

    # dp[i][w] = i번째 물건까지 고려하고, 배낭 용량이 w일 때의 최대 가치
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 각 물건을 순회 (1-indexed)
    for i in range(1, n + 1):
        # 각 배낭 용량을 순회
        for w in range(capacity + 1):
            # 현재 물건을 넣지 않는 경우 (이전 물건까지의 최대 가치)
            dp[i][w] = dp[i - 1][w]

            # 현재 물건의 무게가 배낭 용량 이하이면 넣을 수 있음
            if weights[i - 1] <= w:
                # 넣는 경우 vs 안 넣는 경우 중 큰 값 선택
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )

    # 모든 물건을 고려하고 전체 용량일 때의 최대 가치 반환
    return dp[n][capacity]


# === 실행 예제 ===
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    result = knapsack(weights, values, capacity)
    print(f"물건 무게: {weights}")
    print(f"물건 가치: {values}")
    print(f"배낭 용량: {capacity}")
    print(f"최대 가치: {result}")
