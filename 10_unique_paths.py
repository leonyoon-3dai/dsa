"""
Dynamic Programming Example 10: Unique Paths (고유 경로)

Problem: m x n 격자의 왼쪽 상단에서 오른쪽 하단까지 이동하는 경로의 수를 구하라.
         이동은 오른쪽 또는 아래쪽으로만 가능하다.
LeetCode #62
"""


def unique_paths(m: int, n: int) -> int:
    # dp[i][j] = (i, j) 위치에 도달하는 경로의 수
    dp = [[1] * n for _ in range(m)]

    # 첫 번째 행과 첫 번째 열은 모두 1 (한 방향으로만 갈 수 있으므로)
    # 이미 1로 초기화됨

    # (1,1)부터 (m-1, n-1)까지 순회
    for i in range(1, m):
        for j in range(1, n):
            # 위에서 오는 경로 + 왼쪽에서 오는 경로
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # 우하단 도달 경로 수 반환
    return dp[m - 1][n - 1]


# === 실행 예제 ===
if __name__ == "__main__":
    print(f"3x7 격자: {unique_paths(3, 7)}가지 경로")  # 출력: 28
    print(f"3x3 격자: {unique_paths(3, 3)}가지 경로")  # 출력: 6
