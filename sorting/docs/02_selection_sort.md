# 02. Selection Sort (선택 정렬)

## 문제 정의

주어진 배열을 오름차순으로 정렬하라.

```
정렬되지 않은 부분에서 최솟값을 찾아
정렬된 부분의 끝에 배치하는 과정을 반복한다.
```

매 단계에서 "선택"하여 올바른 위치에 놓는다는 의미에서 선택 정렬이라 한다.

---

## 접근법 1: 기본 선택 정렬

정렬되지 않은 구간에서 최솟값을 찾아 교환합니다.

```python
def selection_sort_basic(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
result = arr[:]
n = len(result)
```
- 원본 배열을 보호하기 위해 복사본을 생성합니다.
- 배열 길이를 `n`에 저장합니다.

```python
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if result[j] < result[min_idx]:
            min_idx = j
    result[i], result[min_idx] = result[min_idx], result[i]
```
- 외부 루프: `i`는 현재 정렬할 위치를 나타냅니다.
- `min_idx = i`: 현재 위치를 임시 최솟값으로 설정합니다.
- 내부 루프: `i+1`부터 끝까지 탐색하여 더 작은 값을 찾습니다.
- 최솟값을 찾은 후, 현재 위치(`i`)와 교환합니다.

### 실행 예제: arr = [64, 25, 12, 22, 11]

```
i=0: 최솟값 탐색 [64, 25, 12, 22, 11] → min_idx=4 (11)
     교환: [11, 25, 12, 22, 64]

i=1: 최솟값 탐색 [_, 25, 12, 22, 64] → min_idx=2 (12)
     교환: [11, 12, 25, 22, 64]

i=2: 최솟값 탐색 [_, _, 25, 22, 64] → min_idx=3 (22)
     교환: [11, 12, 22, 25, 64]

i=3: 최솟값 탐색 [_, _, _, 25, 64] → min_idx=3 (25)
     교환 없음: [11, 12, 22, 25, 64]

결과: [11, 12, 22, 25, 64]
```

---

## 접근법 2: 안정 선택 정렬

교환 대신 삽입 방식을 사용하여 안정 정렬(stable sort)을 구현합니다.

```python
def selection_sort_stable(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
min_val = result[min_idx]
while min_idx > i:
    result[min_idx] = result[min_idx - 1]
    min_idx -= 1
result[i] = min_val
```
- 교환(swap) 대신, 최솟값 위치부터 현재 위치까지 원소를 한 칸씩 뒤로 밀어냅니다.
- 그런 다음 최솟값을 현재 위치에 삽입합니다.
- 이 방식은 같은 값의 원소 간 **상대적 순서를 보존**합니다.
- 기본 선택 정렬은 교환 시 안정성이 깨질 수 있지만, 이 방식은 안정적입니다.

### 실행 예제: arr = [3a, 2, 3b, 1] (3a와 3b는 같은 값)

```
기본 선택 정렬: [1, 2, 3b, 3a] → 3a와 3b의 순서가 바뀜 (불안정)
안정 선택 정렬: [1, 2, 3a, 3b] → 3a와 3b의 순서가 유지됨 (안정)
```

---

## 접근법 3: 양방향 선택 정렬 (Double Selection Sort)

한 번의 패스에서 최솟값과 최댓값을 동시에 찾습니다.

```python
def selection_sort_bidirectional(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
left = 0
right = n - 1
while left < right:
    min_idx = left
    max_idx = left
    for i in range(left, right + 1):
        if result[i] < result[min_idx]:
            min_idx = i
        if result[i] > result[max_idx]:
            max_idx = i
```
- `left`와 `right`가 양쪽 경계를 나타냅니다.
- 한 번의 순회로 최솟값과 최댓값의 인덱스를 동시에 찾습니다.

```python
result[left], result[min_idx] = result[min_idx], result[left]
if max_idx == left:
    max_idx = min_idx
result[right], result[max_idx] = result[max_idx], result[right]
left += 1
right -= 1
```
- 최솟값을 왼쪽 경계로, 최댓값을 오른쪽 경계로 이동합니다.
- **주의**: `max_idx == left`이면 첫 번째 교환으로 최댓값 위치가 변경되었으므로 보정합니다.
- 경계를 한 칸씩 좁혀나갑니다.

### 실행 예제: arr = [64, 25, 12, 22, 11]

```
left=0, right=4:
  min=11(idx=4), max=64(idx=0)
  교환 min→left: [11, 25, 12, 22, 64]
  max_idx가 left였으므로 max_idx=4로 보정
  교환 max→right: [11, 25, 12, 22, 64]

left=1, right=3:
  min=12(idx=2), max=25(idx=1)
  교환 min→left: [11, 12, 25, 22, 64]
  교환 max→right: [11, 12, 22, 25, 64]

left=2, right=2: left >= right → 종료

결과: [11, 12, 22, 25, 64]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 (최선) | 시간 복잡도 (평균) | 시간 복잡도 (최악) | 공간 복잡도 |
|--------|-------------------|-------------------|-------------------|------------|
| 기본 선택 정렬 | O(n²) | O(n²) | O(n²) | O(1) |
| 안정 선택 정렬 | O(n²) | O(n²) | O(n²) | O(1) |
| 양방향 선택 정렬 | O(n²) | O(n²) | O(n²) | O(1) |
