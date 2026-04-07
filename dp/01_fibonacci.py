"""
Dynamic Programming Example 1: Fibonacci Number
피보나치 수열 - DP의 가장 기본적인 예제

Problem: n번째 피보나치 수를 구하라.
F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
"""


def fibonacci_top_down(n: int, memo: dict = None) -> int:
    # memo가 None이면 빈 딕셔너리로 초기화 (메모이제이션 저장소)
    if memo is None:
        memo = {}

    # Base case: n이 0이면 0을 반환
    if n == 0:
        return 0

    # Base case: n이 1이면 1을 반환
    if n == 1:
        return 1

    # 이미 계산한 값이 memo에 있으면 바로 반환 (중복 계산 방지)
    if n in memo:
        return memo[n]

    # F(n) = F(n-1) + F(n-2)를 재귀적으로 계산하고 memo에 저장
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)

    # 계산된 결과를 반환
    return memo[n]


def fibonacci_bottom_up(n: int) -> int:
    # Base case: n이 0 이하이면 0을 반환
    if n <= 0:
        return 0

    # Base case: n이 1이면 1을 반환
    if n == 1:
        return 1

    # DP 테이블을 n+1 크기로 생성하고 0으로 초기화
    dp = [0] * (n + 1)

    # F(0) = 0, F(1) = 1로 초기값 설정
    dp[0] = 0
    dp[1] = 1

    # 2부터 n까지 반복하며 DP 테이블을 채움
    for i in range(2, n + 1):
        # 현재 값 = 이전 두 값의 합
        dp[i] = dp[i - 1] + dp[i - 2]

    # n번째 피보나치 수를 반환
    return dp[n]


def fibonacci_space_optimized(n: int) -> int:
    # Base case 처리
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # 두 개의 변수만 사용하여 공간 복잡도를 O(1)로 최적화
    prev2 = 0  # F(i-2)를 저장
    prev1 = 1  # F(i-1)를 저장

    # 2부터 n까지 반복
    for i in range(2, n + 1):
        # 현재 값 = 이전 두 값의 합
        current = prev1 + prev2
        # 변수를 한 칸씩 앞으로 이동
        prev2 = prev1
        prev1 = current

    # 최종 결과 반환
    return prev1


# === 실행 예제 ===
if __name__ == "__main__":
    # n = 10일 때 피보나치 수를 세 가지 방법으로 계산
    n = 10
    print(f"Fibonacci({n}) Top-Down:        {fibonacci_top_down(n)}")
    print(f"Fibonacci({n}) Bottom-Up:       {fibonacci_bottom_up(n)}")
    print(f"Fibonacci({n}) Space Optimized: {fibonacci_space_optimized(n)}")

    # n = 0부터 15까지의 피보나치 수열 출력
    print("\nFibonacci Sequence (0~15):")
    for i in range(16):
        print(f"  F({i:2d}) = {fibonacci_bottom_up(i)}")
