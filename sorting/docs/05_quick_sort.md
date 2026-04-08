# 05. Quick Sort (퀵 정렬)

## 문제 정의

주어진 배열을 오름차순으로 정렬하라.

```
피벗(pivot) 원소를 선택하고,
피벗보다 작은 것은 왼쪽, 큰 것은 오른쪽에 배치한 뒤
각 부분을 재귀적으로 정렬한다.
```

평균적으로 가장 빠른 비교 기반 정렬 알고리즘이다.

---

## 접근법 1: Lomuto 파티션 퀵 정렬

마지막 원소를 피벗으로 사용하는 Lomuto 파티션 방식입니다.

```python
def quick_sort_lomuto(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
def _partition_lomuto(arr, low, high):
    pivot = arr[high]
    i = low - 1
```
- 마지막 원소 `arr[high]`를 피벗으로 선택합니다.
- `i`는 "피벗보다 작은 원소들의 영역" 경계를 가리킵니다.

```python
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
```
- `j`가 `low`부터 `high-1`까지 순회합니다.
- `arr[j] <= pivot`이면 경계 `i`를 오른쪽으로 확장하고 원소를 교환합니다.
- 결과적으로 `[low, i]`에는 피벗 이하의 원소, `[i+1, high-1]`에는 피벗 초과의 원소가 배치됩니다.

```python
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```
- 피벗을 `i+1` 위치에 배치합니다. 이것이 피벗의 최종 위치입니다.

```python
def _sort(arr, low, high):
    if low >= high:
        return
    pivot_idx = _partition_lomuto(arr, low, high)
    _sort(arr, low, pivot_idx - 1)
    _sort(arr, pivot_idx + 1, high)
```
- 파티션 후 피벗의 왼쪽과 오른쪽을 각각 재귀적으로 정렬합니다.

### 실행 예제: arr = [10, 7, 8, 9, 1, 5]

```
_partition(arr, 0, 5), pivot=5:
  j=0: 10>5 → 건너뜀
  j=1: 7>5 → 건너뜀
  j=2: 8>5 → 건너뜀
  j=3: 9>5 → 건너뜀
  j=4: 1<=5 → i=0, swap → [1, 7, 8, 9, 10, 5]
  피벗 배치: [1, 5, 8, 9, 10, 7]  pivot_idx=1

왼쪽 [1]: 크기 1 → 정렬 완료
오른쪽 [8, 9, 10, 7]: 재귀적으로 정렬 → [7, 8, 9, 10]

결과: [1, 5, 7, 8, 9, 10]
```

---

## 접근법 2: Hoare 파티션 퀵 정렬

양쪽에서 포인터가 접근하는 Hoare 파티션 방식입니다. Lomuto보다 평균 교환 횟수가 적습니다.

```python
def quick_sort_hoare(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
def _partition_hoare(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
```
- 첫 번째 원소를 피벗으로 선택합니다.
- `i`는 왼쪽에서, `j`는 오른쪽에서 출발하여 서로 접근합니다.

```python
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
```
- `i`는 피벗보다 크거나 같은 원소를 찾을 때까지 오른쪽으로 이동합니다.
- `j`는 피벗보다 작거나 같은 원소를 찾을 때까지 왼쪽으로 이동합니다.
- 두 포인터가 교차하면 분할 완료, 아니면 두 원소를 교환합니다.
- **차이점**: Hoare 파티션은 `j`를 반환하고, 재귀 구간이 `[low, p]`와 `[p+1, high]`입니다.

### 실행 예제: arr = [8, 3, 5, 1, 9]

```
pivot=8, i=-1, j=5:
  i→0 (arr[0]=8, 8>=8 멈춤)
  j→3 (arr[4]=9>8, arr[3]=1<8 멈춤)
  swap: [1, 3, 5, 8, 9]
  i→3 (arr[1]=3<8, arr[2]=5<8, arr[3]=8>=8 멈춤)
  j→2 (arr[3]=8>=8? 아니 8>8이 아님, arr[2]=5<8 멈춤)
  i(3) >= j(2) → return 2

왼쪽 [1, 3, 5], 오른쪽 [8, 9]

결과: [1, 3, 5, 8, 9]
```

---

## 접근법 3: 3-Way 파티션 퀵 정렬

중복 원소가 많을 때 효과적인 3-way 파티션입니다. (Dutch National Flag 알고리즘)

```python
def quick_sort_three_way(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
rand_idx = random.randint(low, high)
arr[low], arr[rand_idx] = arr[rand_idx], arr[low]
pivot = arr[low]
```
- 랜덤 피벗을 선택하여 최악의 경우(이미 정렬된 배열)를 방지합니다.

```python
lt = low   # 피벗보다 작은 영역의 경계
gt = high  # 피벗보다 큰 영역의 경계
i = low + 1
while i <= gt:
    if arr[i] < pivot:
        arr[lt], arr[i] = arr[i], arr[lt]
        lt += 1
        i += 1
    elif arr[i] > pivot:
        arr[i], arr[gt] = arr[gt], arr[i]
        gt -= 1
    else:
        i += 1
```
- 배열을 세 구간으로 분할합니다:
  - `[low, lt-1]`: 피벗보다 **작은** 원소
  - `[lt, gt]`: 피벗과 **같은** 원소
  - `[gt+1, high]`: 피벗보다 **큰** 원소
- 피벗과 같은 원소는 재귀 호출에서 제외되므로 중복이 많을수록 효율적입니다.

### 실행 예제: arr = [3, 1, 2, 3, 1, 2, 3]

```
pivot=3 (랜덤 선택), lt=0, gt=6, i=1:
  arr[1]=1 < 3: swap, lt=1, i=2
  arr[2]=2 < 3: swap, lt=2, i=3
  arr[3]=3 = 3: i=4
  arr[4]=1 < 3: swap, lt=3, i=5
  arr[5]=2 < 3: swap, lt=4, i=6
  arr[6]=3 = 3: i=7 > gt → 종료

분할 결과: [1, 2, 1, 2 | 3, 3, 3]
왼쪽 [1, 2, 1, 2] 재귀 정렬 → [1, 1, 2, 2]
오른쪽 []: 없음

결과: [1, 1, 2, 2, 3, 3, 3]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 (최선) | 시간 복잡도 (평균) | 시간 복잡도 (최악) | 공간 복잡도 |
|--------|-------------------|-------------------|-------------------|------------|
| Lomuto 파티션 | O(n log n) | O(n log n) | O(n²) | O(log n) 호출 스택 |
| Hoare 파티션 | O(n log n) | O(n log n) | O(n²) | O(log n) 호출 스택 |
| 3-Way 파티션 | O(n) 중복 많을 때 | O(n log n) | O(n²) | O(log n) 호출 스택 |
