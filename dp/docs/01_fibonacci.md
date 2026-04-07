# 01. Fibonacci (피보나치 수열)

## 문제 정의

n번째 피보나치 수를 구하라.

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)  (n >= 2)
```

피보나치 수열: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...`

---

## 접근법 1: Top-Down (메모이제이션)

재귀 + 딕셔너리 캐시를 사용합니다.

```python
def fibonacci_top_down(n: int, memo: dict = None) -> int:
```

### 라인별 설명

```python
if memo is None:
    memo = {}
```
- `memo`가 `None`이면 빈 딕셔너리로 초기화합니다.
- 이 딕셔너리가 **메모이제이션 저장소** 역할을 합니다.
- 이미 계산한 결과를 저장해서 중복 계산을 방지합니다.

```python
if n == 0:
    return 0
if n == 1:
    return 1
```
- **Base Case**: F(0) = 0, F(1) = 1
- 재귀의 종료 조건입니다. 이것이 없으면 무한 재귀에 빠집니다.

```python
if n in memo:
    return memo[n]
```
- `n`이 이미 memo에 있으면 저장된 값을 바로 반환합니다.
- **핵심 최적화**: 이 한 줄이 시간복잡도를 O(2^n) → O(n)으로 줄입니다.

```python
memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
return memo[n]
```
- F(n) = F(n-1) + F(n-2)를 재귀적으로 계산합니다.
- 결과를 `memo[n]`에 저장한 후 반환합니다.

### 실행 예제

```
fibonacci_top_down(5)
  → fibonacci_top_down(4) + fibonacci_top_down(3)
  → (fibonacci_top_down(3) + fibonacci_top_down(2)) + ...
  → memo 활용으로 각 값은 한 번만 계산됨

F(5) = 5
```

---

## 접근법 2: Bottom-Up (타뷸레이션)

배열을 앞에서부터 채워나갑니다.

```python
def fibonacci_bottom_up(n: int) -> int:
```

### 라인별 설명

```python
if n <= 0:
    return 0
if n == 1:
    return 1
```
- Base case 처리: n이 0 이하면 0, 1이면 1을 반환합니다.

```python
dp = [0] * (n + 1)
```
- 크기 `n+1`의 배열을 0으로 초기화합니다.
- `dp[i]`는 i번째 피보나치 수를 저장합니다.

```python
dp[0] = 0
dp[1] = 1
```
- 초기값 설정: F(0) = 0, F(1) = 1

```python
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
```
- 2부터 n까지 반복하며 점화식 `F(i) = F(i-1) + F(i-2)`를 적용합니다.
- 이전 값들이 이미 계산되어 있으므로 바로 참조 가능합니다.

### 실행 예제: n = 6

```
dp = [0, 1, 0, 0, 0, 0, 0]

i=2: dp[2] = dp[1] + dp[0] = 1 + 0 = 1   → [0, 1, 1, 0, 0, 0, 0]
i=3: dp[3] = dp[2] + dp[1] = 1 + 1 = 2   → [0, 1, 1, 2, 0, 0, 0]
i=4: dp[4] = dp[3] + dp[2] = 2 + 1 = 3   → [0, 1, 1, 2, 3, 0, 0]
i=5: dp[5] = dp[4] + dp[3] = 3 + 2 = 5   → [0, 1, 1, 2, 3, 5, 0]
i=6: dp[6] = dp[5] + dp[4] = 5 + 3 = 8   → [0, 1, 1, 2, 3, 5, 8]

결과: F(6) = 8
```

---

## 접근법 3: 공간 최적화

변수 2개만 사용하여 O(1) 공간으로 해결합니다.

```python
prev2 = 0  # F(i-2)
prev1 = 1  # F(i-1)
```
- 배열 대신 변수 2개만 유지합니다.

```python
for i in range(2, n + 1):
    current = prev1 + prev2
    prev2 = prev1
    prev1 = current
```
- `current = prev1 + prev2`: 현재 값 계산
- `prev2 = prev1`: 한 칸 이동
- `prev1 = current`: 한 칸 이동

### 실행 예제: n = 5

```
초기: prev2=0, prev1=1

i=2: current=1+0=1, prev2=1, prev1=1
i=3: current=1+1=2, prev2=1, prev1=2
i=4: current=2+1=3, prev2=2, prev1=3
i=5: current=3+2=5, prev2=3, prev1=5

결과: F(5) = 5
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 순수 재귀 (메모이제이션 없음) | O(2^n) | O(n) 호출 스택 |
| Top-Down (메모이제이션) | O(n) | O(n) memo + 호출 스택 |
| Bottom-Up (타뷸레이션) | O(n) | O(n) dp 배열 |
| 공간 최적화 | O(n) | O(1) |
