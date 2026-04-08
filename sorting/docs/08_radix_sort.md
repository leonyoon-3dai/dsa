# 08. Radix Sort (기수 정렬)

## 문제 정의

주어진 배열을 오름차순으로 정렬하라.

```
각 자릿수별로 안정 정렬(계수 정렬)을 반복 적용하여 정렬한다.
비교 기반이 아닌 정렬로, 자릿수 d와 기수 k에 대해 O(d(n+k)) 시간에 동작한다.
```

정수나 문자열처럼 자릿수로 분해할 수 있는 데이터에 적합하다.

---

## 접근법 1: LSD 기수 정렬 (Least Significant Digit)

가장 낮은 자릿수부터 정렬합니다. 가장 일반적인 기수 정렬 방식입니다.

```python
def radix_sort_lsd(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
if not arr:
    return []
result = arr[:]
max_val = max(result)
```
- 빈 배열 처리 후, 최댓값을 구하여 필요한 자릿수를 결정합니다.

```python
exp = 1
while max_val // exp > 0:
    result = _counting_sort_by_digit(result, exp)
    exp *= 10
```
- `exp`: 현재 처리 중인 자릿수 (1=일의 자리, 10=십의 자리, 100=백의 자리, ...)
- 최댓값의 모든 자릿수를 처리할 때까지 반복합니다.
- 매 자릿수마다 안정 계수 정렬을 적용합니다.
- **핵심**: 안정 정렬이어야 이전 자릿수의 정렬 순서가 유지됩니다.

**_counting_sort_by_digit 함수:**

```python
def _counting_sort_by_digit(arr, exp):
    n = len(arr)
    result = [0] * n
    count = [0] * 10
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        result[count[digit]] = arr[i]
    return result
```
- `(num // exp) % 10`: 특정 자릿수의 숫자를 추출합니다.
- 0~9에 대한 카운팅, 누적합 계산, 뒤에서부터 배치를 수행합니다.

### 실행 예제: arr = [170, 45, 75, 90, 802, 24, 2, 66]

```
1의 자리 (exp=1) 기준 정렬:
  자릿수: [0, 5, 5, 0, 2, 4, 2, 6]
  결과: [170, 90, 802, 2, 24, 45, 75, 66]

10의 자리 (exp=10) 기준 정렬:
  자릿수: [7, 9, 0, 0, 2, 4, 7, 6]
  결과: [802, 2, 24, 45, 66, 170, 75, 90]

100의 자리 (exp=100) 기준 정렬:
  자릿수: [8, 0, 0, 0, 0, 1, 0, 0]
  결과: [2, 24, 45, 66, 75, 90, 170, 802]

결과: [2, 24, 45, 66, 75, 90, 170, 802]
```

---

## 접근법 2: MSD 기수 정렬 (Most Significant Digit)

가장 높은 자릿수부터 정렬합니다. 재귀적으로 각 버킷을 처리합니다.

```python
def radix_sort_msd(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
max_val = max(result)
max_digits = len(str(max_val))
exp = 10 ** (max_digits - 1)
```
- 최댓값의 자릿수를 계산합니다.
- 가장 높은 자릿수에 해당하는 `exp`를 구합니다.

```python
def _msd_sort(arr, exp):
    if len(arr) <= 1 or exp <= 0:
        return arr
    buckets = [[] for _ in range(10)]
    for num in arr:
        digit = (num // exp) % 10
        buckets[digit].append(num)
    result = []
    for bucket in buckets:
        result.extend(_msd_sort(bucket, exp // 10))
    return result
```
- **Base Case**: 배열 크기가 1 이하이거나 모든 자릿수를 처리했으면 반환합니다.
- 현재 자릿수의 숫자에 따라 10개의 버킷에 분배합니다.
- 각 버킷을 다음 자릿수 기준으로 재귀적으로 정렬합니다.
- **LSD와의 차이**: MSD는 재귀적이고, 큰 자릿수가 같은 원소끼리만 비교합니다.

### 실행 예제: arr = [170, 45, 75, 90, 802]

```
100의 자리 (exp=100):
  버킷 0: [45, 75, 90]  (100의 자리가 0)
  버킷 1: [170]
  버킷 8: [802]

버킷 0을 10의 자리 (exp=10)로 재귀:
  버킷 4: [45]
  버킷 7: [75]
  버킷 9: [90]
  → [45, 75, 90]

결과: [45, 75, 90, 170, 802]
```

---

## 접근법 3: 음수 지원 기수 정렬

음수를 양수로 변환하여 처리한 후 다시 합칩니다.

```python
def radix_sort_negative(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
negatives = [-x for x in arr if x < 0]
positives = [x for x in arr if x >= 0]
```
- 음수와 양수를 분리합니다.
- 음수는 부호를 뒤집어 양수로 변환합니다.

```python
sorted_pos = radix_sort_lsd(positives) if positives else []
sorted_neg = radix_sort_lsd(negatives) if negatives else []
sorted_neg = [-x for x in reversed(sorted_neg)]
return sorted_neg + sorted_pos
```
- 양수와 (변환된) 음수를 각각 기수 정렬합니다.
- 음수 결과를 다시 음수로 변환하고 **역순**으로 뒤집습니다.
  - 예: `[-1, -3, -5]` → 양수화: `[1, 3, 5]` → 정렬: `[1, 3, 5]` → 역순+음수화: `[-5, -3, -1]`
- 음수 부분 + 양수 부분을 합쳐서 반환합니다.

### 실행 예제: arr = [170, -45, 75, -90]

```
음수 (양수화): [45, 90]
양수: [170, 75]

LSD 정렬:
  양수: [75, 170]
  음수(양수화): [45, 90]

음수 복원 (역순 + 부호 반전):
  [90, 45] → [-90, -45]

결과: [-90, -45, 75, 170]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 | 안정 정렬 |
|--------|------------|------------|----------|
| LSD 기수 정렬 | O(d × (n + k)) | O(n + k) | 예 |
| MSD 기수 정렬 | O(d × (n + k)) | O(n + k + d) 재귀 | 예 |
| 음수 지원 | O(d × (n + k)) | O(n + k) | 예 |

- `d`: 최댓값의 자릿수, `n`: 배열 크기, `k`: 기수 (보통 10)
