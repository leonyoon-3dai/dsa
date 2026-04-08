# 08. Interval Scheduling / Merge Intervals (구간 스케줄링)

## 문제 정의

**문제 1 (Merge Intervals)**: 겹치는 구간들을 병합하라. (LeetCode #56)

```
입력: [[1,3], [2,6], [8,10], [15,18]]
출력: [[1,6], [8,10], [15,18]]
```

**문제 2 (Non-overlapping Intervals)**: 겹치지 않게 만들기 위해 제거해야 할 최소 구간 수. (LeetCode #435)

---

## 접근법 1: 구간 병합 (Merge Intervals)

시작 시간 기준 정렬 후, 순회하면서 겹치는 구간을 합친다.

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
```

### 라인별 설명

```python
intervals.sort(key=lambda x: x[0])
```
- **시작 시간 기준** 오름차순 정렬합니다.
- 정렬하면 겹칠 수 있는 구간들이 연속으로 나열됩니다.

```python
merged = [intervals[0]]
```
- 결과 리스트를 첫 번째 구간으로 초기화합니다.

```python
for i in range(1, len(intervals)):
    start = intervals[i][0]
    end = intervals[i][1]
    last_end = merged[-1][1]

    if start <= last_end:
        merged[-1][1] = max(last_end, end)
    else:
        merged.append([start, end])
```
- 현재 구간의 시작이 마지막 병합 구간의 끝 **이하**이면 겹침.
- 겹치면 끝을 더 큰 값으로 **확장**합니다.
- 겹치지 않으면 새 구간으로 추가합니다.

### 실행 예제

```
정렬 후: [[1,3], [2,6], [8,10], [15,18]]
merged = [[1,3]]

[2,6]: start=2 <= 3 → 겹침. merged[-1][1] = max(3,6) = 6
  merged = [[1,6]]

[8,10]: start=8 > 6 → 안 겹침. 추가.
  merged = [[1,6], [8,10]]

[15,18]: start=15 > 10 → 안 겹침. 추가.
  merged = [[1,6], [8,10], [15,18]]
```

---

## 접근법 2: 최대 비겹침 구간 선택

종료 시간 기준 정렬 후, 겹치지 않는 구간을 최대한 많이 선택한다.

```python
def max_non_overlapping(intervals: list[list[int]]) -> list[list[int]]:
```

### 라인별 설명

```python
sorted_intervals = sorted(intervals, key=lambda x: x[1])
```
- **종료 시간 기준** 오름차순 정렬합니다.
- 활동 선택 문제와 동일한 원리: 일찍 끝나는 것을 우선 선택합니다.

```python
selected = [sorted_intervals[0]]
last_end = sorted_intervals[0][1]

for i in range(1, len(sorted_intervals)):
    if sorted_intervals[i][0] >= last_end:
        selected.append(sorted_intervals[i])
        last_end = sorted_intervals[i][1]
```
- 현재 구간의 시작이 마지막 선택의 종료 **이상**이면 선택합니다.
- 종료 시간을 갱신합니다.

### 실행 예제

```
입력: [[1,4], [2,3], [3,6], [5,7], [6,8]]
종료 기준 정렬: [[2,3], [1,4], [3,6], [5,7], [6,8]]

선택: [2,3], last_end=3
[1,4]: 1 < 3 → 건너뜀
[3,6]: 3 >= 3 → 선택! last_end=6
[5,7]: 5 < 6 → 건너뜀
[6,8]: 6 >= 6 → 선택! last_end=8

결과: [[2,3], [3,6], [6,8]] → 3개
```

---

## 접근법 3: 최소 제거 수

겹치지 않게 만들기 위해 제거해야 할 최소 구간 수를 구한다.

```python
def min_removals_for_non_overlapping(intervals: list[list[int]]) -> int:
```

### 라인별 설명

```python
intervals.sort(key=lambda x: x[1])
keep_count = 1
last_end = intervals[0][1]

for i in range(1, len(intervals)):
    if intervals[i][0] >= last_end:
        keep_count += 1
        last_end = intervals[i][1]

return len(intervals) - keep_count
```
- 유지할 수 있는 최대 구간 수를 구한 뒤, 전체에서 빼면 제거해야 할 수입니다.
- `keep_count`는 접근법 2와 동일한 로직으로 계산합니다.

### 실행 예제

```
입력: [[1,2], [2,3], [3,4], [1,3]]
종료 기준 정렬: [[1,2], [2,3], [1,3], [3,4]]

keep: [1,2], last_end=2
[2,3]: 2 >= 2 → 유지. keep=2, last_end=3
[1,3]: 1 < 3 → 제거
[3,4]: 3 >= 3 → 유지. keep=3, last_end=4

제거 수: 4 - 3 = 1
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 구간 병합 | O(n log n) | O(n) |
| 최대 비겹침 선택 | O(n log n) | O(n) |
| 최소 제거 수 | O(n log n) | O(1) 정렬 제외 |
