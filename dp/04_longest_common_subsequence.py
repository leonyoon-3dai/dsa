"""
Dynamic Programming Example 4: Longest Common Subsequence (최장 공통 부분 수열)

Problem: 두 문자열이 주어질 때, 가장 긴 공통 부분 수열의 길이를 구하라.
LeetCode #1143
"""


def lcs(text1: str, text2: str) -> int:
    # 두 문자열의 길이를 저장
    m = len(text1)
    n = len(text2)

    # dp[i][j] = text1[:i]와 text2[:j]의 LCS 길이
    # (m+1) x (n+1) 크기의 2D 배열을 0으로 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # text1의 각 문자를 순회 (1-indexed)
    for i in range(1, m + 1):
        # text2의 각 문자를 순회 (1-indexed)
        for j in range(1, n + 1):
            # 두 문자가 같으면 대각선 값 + 1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 다르면 위쪽 또는 왼쪽 값 중 큰 값을 선택
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 전체 두 문자열의 LCS 길이를 반환
    return dp[m][n]


# === 실행 예제 ===
if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(f'text1 = "{text1}", text2 = "{text2}"')
    print(f"LCS 길이: {lcs(text1, text2)}")  # 출력: 3 ("ace")

    text1 = "AGGTAB"
    text2 = "GXTXAYB"
    print(f'\ntext1 = "{text1}", text2 = "{text2}"')
    print(f"LCS 길이: {lcs(text1, text2)}")  # 출력: 4 ("GTAB")
