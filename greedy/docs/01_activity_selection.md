# 01. Activity Selection (활동 선택 문제)

## 문제 정의

시작 시간과 종료 시간이 주어진 활동들 중에서, 서로 겹치지 않는 최대 개수의 활동을 선택하라.

```
입력: activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
출력: [(1,4), (5,7), (8,11), (12,16)]  (최대 4개)
```

---

## 접근법 1: 그리디 (종료 시간 기준 정렬)

종료 시간이 빠른 활동부터 선택하면 남은 시간이 최대화된다.

```python
def activity_selection_greedy(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
```

### 라인별 설명

```python
sorted_acts = sorted(activities, key=lambda x: x[1])
```
- 종료 시간(`x[1]`) 기준으로 **오름차순 정렬**합니다.
- 종료가 빠른 활동을 먼저 선택해야 남은 시간에 더 많은 활동을 넣을 수 있습니다.

```python
selected = [sorted_acts[0]]
last_end = sorted_acts[0][1]
```
- 정렬 후 첫 번째 활동은 **무조건 선택**합니다 (종료가 가장 빠름).
- `last_end`에 마지막으로 선택한 활동의 종료 시간을 기록합니다.

```python
for i in range(1, len(sorted_acts)):
    start = sorted_acts[i][0]
    end = sorted_acts[i][1]
    if start >= last_end:
        selected.append((start, end))
        last_end = end
```
- 나머지 활동을 순회하면서, **시작 시간이 마지막 종료 시간 이후**인 활동만 선택합니다.
- 선택할 때마다 `last_end`를 갱신합니다.

### 실행 예제

```
정렬 후: [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]

1. 선택: (1,4), last_end=4
2. (3,5): start=3 < 4 → 건너뜀
3. (0,6): start=0 < 4 → 건너뜀
4. (5,7): start=5 >= 4 → 선택! last_end=7
5. (3,9): start=3 < 7 → 건너뜀
6. (5,9): start=5 < 7 → 건너뜀
7. (6,10): start=6 < 7 → 건너뜀
8. (8,11): start=8 >= 7 → 선택! last_end=11
9. (8,12): start=8 < 11 → 건너뜀
10. (2,14): start=2 < 11 → 건너뜀
11. (12,16): start=12 >= 11 → 선택! last_end=16

결과: [(1,4), (5,7), (8,11), (12,16)] → 4개
```

---

## 접근법 2: DP (동적 프로그래밍)

각 활동에 대해 "선택/비선택"을 고려하여 최대 개수를 구한다.

```python
def activity_selection_dp(activities: list[tuple[int, int]]) -> int:
```

### 라인별 설명

```python
sorted_acts = sorted(activities, key=lambda x: x[1])
dp = [0] * n
dp[0] = 1
```
- 종료 시간 기준으로 정렬합니다.
- `dp[i]`는 0~i번째 활동까지 고려했을 때의 **최대 선택 가능 수**입니다.
- 첫 번째 활동은 항상 1개 선택 가능합니다.

```python
for i in range(1, n):
    exclude = dp[i - 1]
    include = 1
    for j in range(i - 1, -1, -1):
        if sorted_acts[j][1] <= start_i:
            include = dp[j] + 1
            break
    dp[i] = max(exclude, include)
```
- `exclude`: 현재 활동을 선택하지 않는 경우 (이전까지의 최대값).
- `include`: 현재 활동을 선택하는 경우, 겹치지 않는 마지막 활동의 dp 값 + 1.
- 둘 중 큰 값을 `dp[i]`에 저장합니다.

### 실행 예제

```
정렬 후: [(1,4), (3,5), (0,6), (5,7), ...]
dp[0] = 1  (첫 활동 선택)
dp[1] = max(dp[0], 1) = 1  (3,5)는 (1,4)와 겹침
dp[2] = max(dp[1], 1) = 1  (0,6)도 겹침
dp[3] = max(dp[2], dp[0]+1) = max(1, 2) = 2  (5,7)은 (1,4) 이후 가능
...
```

---

## 접근법 3: 재귀 (탐욕적 재귀)

그리디 선택을 재귀적으로 구현한 버전.

```python
def helper(index: int, last_end: int) -> list[tuple[int, int]]:
```

### 라인별 설명

```python
if index == len(sorted_acts):
    return []
```
- 모든 활동을 확인했으면 빈 리스트를 반환합니다 (재귀 종료).

```python
if start >= last_end:
    return [(start, end)] + helper(index + 1, end)
else:
    return helper(index + 1, last_end)
```
- 현재 활동이 겹치지 않으면 선택 후 다음으로 진행합니다.
- 겹치면 건너뜁니다.

### 실행 예제

```
helper(0, 0) → (1,4) 선택 → helper(1, 4)
helper(1, 4) → (3,5) 건너뜀 → helper(2, 4)
helper(2, 4) → (0,6) 건너뜀 → helper(3, 4)
helper(3, 4) → (5,7) 선택 → helper(4, 7)
...
결과: [(1,4), (5,7), (8,11), (12,16)]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 그리디 (종료 시간 정렬) | O(n log n) | O(n) 정렬 |
| DP | O(n^2) | O(n) dp 배열 |
| 재귀 (탐욕적) | O(n log n) | O(n) 호출 스택 |
