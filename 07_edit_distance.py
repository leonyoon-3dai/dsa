"""
Dynamic Programming Example 7: Edit Distance (편집 거리)

Problem: 두 문자열이 주어질 때, word1을 word2로 변환하기 위한
         최소 연산 횟수를 구하라. (삽입, 삭제, 교체 가능)
LeetCode #72
"""


def edit_distance(word1: str, word2: str) -> int:
    # 두 문자열의 길이
    m = len(word1)
    n = len(word2)

    # dp[i][j] = word1[:i]를 word2[:j]로 변환하는 최소 연산 횟수
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # word1[:i]를 빈 문자열로 변환 → i번 삭제
    for i in range(m + 1):
        dp[i][0] = i

    # 빈 문자열을 word2[:j]로 변환 → j번 삽입
    for j in range(n + 1):
        dp[0][j] = j

    # 각 문자 쌍에 대해 최소 연산 횟수 계산
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 두 문자가 같으면 추가 연산 불필요
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 삽입(dp[i][j-1]), 삭제(dp[i-1][j]), 교체(dp[i-1][j-1]) 중 최소 + 1
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # 삽입
                    dp[i - 1][j],      # 삭제
                    dp[i - 1][j - 1]   # 교체
                )

    # 전체 문자열 변환의 최소 연산 횟수 반환
    return dp[m][n]


# === 실행 예제 ===
if __name__ == "__main__":
    w1, w2 = "horse", "ros"
    print(f'"{w1}" → "{w2}": {edit_distance(w1, w2)}회')  # 출력: 3

    w1, w2 = "intention", "execution"
    print(f'"{w1}" → "{w2}": {edit_distance(w1, w2)}회')  # 출력: 5
