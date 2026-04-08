# 04. Merge Sort (병합 정렬)

## 문제 정의

주어진 배열을 오름차순으로 정렬하라.

```
배열을 반씩 분할한 뒤, 정렬된 부분 배열들을 병합(merge)한다.
분할 정복(Divide and Conquer) 패러다임의 대표적인 예이다.
```

항상 O(n log n)을 보장하는 안정 정렬 알고리즘이다.

---

## 접근법 1: 재귀 병합 정렬 (Top-Down)

배열을 재귀적으로 반씩 나눈 후 병합합니다.

```python
def merge_sort_recursive(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
if len(arr) <= 1:
    return arr[:]
```
- **Base Case**: 배열 크기가 1 이하이면 이미 정렬된 것이므로 복사본을 반환합니다.

```python
mid = len(arr) // 2
left = merge_sort_recursive(arr[:mid])
right = merge_sort_recursive(arr[mid:])
```
- 배열을 반으로 나누어 왼쪽과 오른쪽을 각각 재귀적으로 정렬합니다.
- `arr[:mid]`: 왼쪽 절반
- `arr[mid:]`: 오른쪽 절반

```python
return _merge(left, right)
```
- 정렬된 두 부분 배열을 병합하여 반환합니다.

**_merge 함수:**

```python
result = []
i = 0  # 왼쪽 포인터
j = 0  # 오른쪽 포인터
while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
result.extend(left[i:])
result.extend(right[j:])
```
- 두 포인터를 사용하여 두 배열의 원소를 비교하며 작은 것을 결과에 추가합니다.
- `<=` 비교로 안정 정렬을 보장합니다 (같은 값이면 왼쪽 것이 먼저 옵니다).
- 한쪽 배열이 소진되면 남은 원소를 모두 추가합니다.

### 실행 예제: arr = [38, 27, 43, 3, 9, 82, 10]

```
분할 과정:
  [38, 27, 43, 3, 9, 82, 10]
  → [38, 27, 43]          [3, 9, 82, 10]
  → [38] [27, 43]         [3, 9] [82, 10]
  → [38] [27] [43]        [3] [9] [82] [10]

병합 과정:
  [27] + [43] → [27, 43]
  [38] + [27, 43] → [27, 38, 43]
  [3] + [9] → [3, 9]
  [82] + [10] → [10, 82]
  [3, 9] + [10, 82] → [3, 9, 10, 82]
  [27, 38, 43] + [3, 9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]

결과: [3, 9, 10, 27, 38, 43, 82]
```

---

## 접근법 2: 상향식 병합 정렬 (Bottom-Up)

재귀 없이 작은 단위부터 시작하여 병합 크기를 키워갑니다.

```python
def merge_sort_bottom_up(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
size = 1
while size < n:
    for start in range(0, n, size * 2):
        mid = min(start + size, n)
        end = min(start + size * 2, n)
        merged = _merge(result[start:mid], result[mid:end])
        result[start:start + len(merged)] = merged
    size *= 2
```
- `size`: 현재 병합할 부분 배열의 크기 (1 → 2 → 4 → 8 → ...)
- `start`: 현재 병합 쌍의 시작 위치
- `mid`, `end`: 두 부분 배열의 경계
- 매 단계에서 인접한 `size` 크기의 부분 배열 쌍을 병합합니다.
- `size`를 2배씩 키우면서 전체 배열이 정렬될 때까지 반복합니다.

### 실행 예제: arr = [5, 3, 8, 1]

```
size=1: [5,3] → [3,5]  |  [8,1] → [1,8]  →  [3, 5, 1, 8]
size=2: [3,5] + [1,8] → [1, 3, 5, 8]

결과: [1, 3, 5, 8]
```

---

## 접근법 3: 제자리 병합 정렬

인덱스 기반으로 동작하여 새 배열 생성을 최소화합니다.

```python
def merge_sort_inplace(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
def _sort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    _sort(arr, left, mid)
    _sort(arr, mid + 1, right)
```
- 인덱스 `left`와 `right`로 정렬 범위를 지정합니다.
- 왼쪽 절반 `[left, mid]`과 오른쪽 절반 `[mid+1, right]`을 재귀적으로 정렬합니다.

```python
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    # 남은 원소 추가 후 원래 배열에 복사
    for k in range(len(temp)):
        arr[left + k] = temp[k]
```
- 임시 배열 `temp`에 병합 결과를 저장한 후, 원래 배열에 복사합니다.
- 완전한 제자리는 아니지만, 새 배열 반환 대신 원본 배열을 수정합니다.

---

## 복잡도 비교

| 접근법 | 시간 복잡도 (최선) | 시간 복잡도 (평균) | 시간 복잡도 (최악) | 공간 복잡도 |
|--------|-------------------|-------------------|-------------------|------------|
| 재귀 (Top-Down) | O(n log n) | O(n log n) | O(n log n) | O(n) |
| 상향식 (Bottom-Up) | O(n log n) | O(n log n) | O(n log n) | O(n) |
| 제자리 (In-Place) | O(n log n) | O(n log n) | O(n log n) | O(n) 임시 배열 |
