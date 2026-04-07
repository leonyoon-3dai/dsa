# 03. Coin Change (동전 거스름돈)

## 문제 정의

동전의 종류 `coins`와 목표 금액 `amount`가 주어질 때, amount를 만드는 **최소 동전 개수**를 구하라. 만들 수 없으면 -1을 반환.

- LeetCode #322

---

## 핵심 아이디어

`dp[i]` = 금액 i를 만드는 데 필요한 최소 동전 수

각 금액 i에 대해 모든 동전 종류를 시도하고, 가장 적은 동전을 사용하는 경우를 선택합니다.

**점화식**: `dp[i] = min(dp[i], dp[i - coin] + 1)` (모든 coin에 대해)

---

## 코드 라인별 설명

```python
dp = [amount + 1] * (amount + 1)
```
- DP 테이블을 `amount + 1`로 초기화합니다.
- `amount + 1`은 **불가능한 값** 역할을 합니다.
- 최대 amount개의 1원짜리 동전이면 충분하므로, amount + 1은 절대 나올 수 없는 값입니다.

```python
dp[0] = 0
```
- 금액 0을 만드는 데 필요한 동전 수 = 0개 (아무것도 안 씀)

```python
for i in range(1, amount + 1):
```
- 금액 1부터 amount까지 순회합니다.

```python
    for coin in coins:
```
- 각 동전 종류에 대해 확인합니다.

```python
        if coin <= i:
```
- 동전의 값이 현재 금액 i 이하여야 사용 가능합니다.
- 예: 금액 3에 동전 5는 사용 불가

```python
            dp[i] = min(dp[i], dp[i - coin] + 1)
```
- **핵심 점화식**: 동전 하나를 사용하면 나머지 금액은 `i - coin`
- `dp[i - coin] + 1`: (i-coin)원을 만드는 최소 동전 수 + 현재 동전 1개
- 현재 dp[i]와 비교하여 더 작은 값을 선택

```python
return dp[amount] if dp[amount] <= amount else -1
```
- dp[amount]가 초기값(amount+1)이면 만들 수 없으므로 -1 반환
- 아니면 최소 동전 수를 반환

---

## 실행 예제 1: coins = [1, 5, 10], amount = 11

```
dp 초기화: [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

i=1:  coin=1  → dp[1] = min(12, dp[0]+1) = 1
i=2:  coin=1  → dp[2] = min(12, dp[1]+1) = 2
i=3:  coin=1  → dp[3] = min(12, dp[2]+1) = 3
i=4:  coin=1  → dp[4] = min(12, dp[3]+1) = 4
i=5:  coin=1  → dp[5] = min(12, dp[4]+1) = 5
      coin=5  → dp[5] = min(5, dp[0]+1) = 1   ← 5원 동전 1개!
i=6:  coin=1  → dp[6] = min(12, dp[5]+1) = 2
      coin=5  → dp[6] = min(2, dp[1]+1) = 2
i=7:  coin=1  → dp[7] = 3, coin=5 → dp[7] = 3
i=8:  coin=1  → dp[8] = 4, coin=5 → dp[8] = 4
i=9:  coin=1  → dp[9] = 5, coin=5 → dp[9] = 5
i=10: coin=1  → dp[10] = 6
      coin=5  → dp[10] = min(6, dp[5]+1) = 2
      coin=10 → dp[10] = min(2, dp[0]+1) = 1   ← 10원 1개!
i=11: coin=1  → dp[11] = 2
      coin=5  → dp[11] = min(2, dp[6]+1) = 2
      coin=10 → dp[11] = min(2, dp[1]+1) = 2

결과: 2개 (10원 + 1원)
```

## 실행 예제 2: coins = [2], amount = 3

```
dp = [0, 3, 3, 3]

i=1: coin=2 → 2 > 1이므로 건너뜀 → dp[1] = 3 (불가능)
i=2: coin=2 → dp[2] = min(3, dp[0]+1) = 1
i=3: coin=2 → dp[3] = min(3, dp[1]+1) = min(3, 4) = 3 (불가능)

dp[3] = 3 > amount(3)이므로 → -1 반환
```

**홀수 금액은 2원 동전만으로 만들 수 없습니다.**

## 실행 예제 3: coins = [1, 5, 10, 25], amount = 37

```
37 = 25 + 10 + 1 + 1 → 4개 동전

dp[37] = 4
```

---

## 복잡도

| 항목 | 값 |
|------|-----|
| 시간 복잡도 | O(amount x len(coins)) |
| 공간 복잡도 | O(amount) |
