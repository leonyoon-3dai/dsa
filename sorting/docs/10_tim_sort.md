# 10. Tim Sort (팀 정렬)

## 문제 정의

주어진 배열을 오름차순으로 정렬하라.

```
삽입 정렬과 병합 정렬을 결합한 하이브리드 정렬 알고리즘이다.
실제 데이터에서 자주 나타나는 부분 정렬(run)을 활용하여 효율적으로 정렬한다.
Python의 내장 sort()와 sorted()가 사용하는 알고리즘이다.
```

Tim Peters가 2002년에 Python을 위해 설계하였다.

---

## 접근법 1: Tim Sort 구현

run 단위로 삽입 정렬 후 병합합니다.

```python
def tim_sort(arr: List[int]) -> List[int]:
```

### 라인별 설명

**_calc_min_run 함수:**

```python
def _calc_min_run(n: int) -> int:
    r = 0
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r
```
- 최소 run 크기를 계산합니다.
- `n`을 2로 나누면서 나머지가 있으면 `r`을 1로 설정합니다.
- 결과값은 32~64 사이의 값이 됩니다.
- **목적**: 배열 크기를 min_run으로 나눈 횟수가 2의 거듭제곱이 되거나 약간 작도록 합니다.
  이렇게 하면 병합 단계에서 균형 잡힌 병합이 이루어집니다.

**삽입 정렬 단계:**

```python
for start in range(0, n, min_run):
    end = min(start + min_run - 1, n - 1)
    _insertion_sort_for_tim(result, start, end)
```
- 배열을 `min_run` 크기의 조각(run)으로 나눕니다.
- 각 run에 삽입 정렬을 적용합니다.
- **왜 삽입 정렬인가?**: 작은 배열(32~64개)에서는 삽입 정렬이 오버헤드가 적고 빠릅니다.

**_insertion_sort_for_tim 함수:**

```python
def _insertion_sort_for_tim(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```
- `[left, right]` 범위에 대해 삽입 정렬을 수행합니다.
- 일반 삽입 정렬과 동일하지만, 범위가 제한되어 있습니다.

**병합 단계:**

```python
size = min_run
while size < n:
    for left in range(0, n, size * 2):
        mid = min(left + size - 1, n - 1)
        right = min(left + 2 * size - 1, n - 1)
        if mid < right:
            _merge_for_tim(result, left, mid, right)
    size *= 2
```
- `size`를 `min_run`부터 시작하여 2배씩 증가시킵니다.
- 인접한 run 쌍을 병합합니다.
- `mid < right`: 병합할 두 부분이 모두 존재하는 경우에만 병합합니다.
- 상향식(bottom-up) 병합 정렬과 유사합니다.

**_merge_for_tim 함수:**

```python
def _merge_for_tim(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    i = 0; j = 0; k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
```
- 두 부분 배열을 복사한 뒤, 두 포인터를 사용하여 병합합니다.
- `<=` 비교로 **안정 정렬**을 보장합니다.

### 실행 예제: arr = [5, 21, 7, 23, 19, 10, 12, 1, 15, 8] (min_run=10이라 가정)

```
배열이 작으므로 min_run >= n, 삽입 정렬만으로 정렬됨:

삽입 정렬 (전체 배열):
  i=1: key=21, 5<21 → [5, 21, 7, 23, 19, 10, 12, 1, 15, 8]
  i=2: key=7, 삽입 → [5, 7, 21, 23, 19, 10, 12, 1, 15, 8]
  i=3: key=23, 21<23 → [5, 7, 21, 23, 19, 10, 12, 1, 15, 8]
  i=4: key=19, 삽입 → [5, 7, 19, 21, 23, 10, 12, 1, 15, 8]
  ...
  최종: [1, 5, 7, 8, 10, 12, 15, 19, 21, 23]

결과: [1, 5, 7, 8, 10, 12, 15, 19, 21, 23]
```

큰 배열의 경우 (n=64, min_run=32):

```
Step 1: [0:31]에 삽입 정렬, [32:63]에 삽입 정렬
Step 2: 두 정렬된 run을 병합

결과: 전체 배열 정렬 완료
```

---

## 접근법 2: 단순화된 Tim Sort

고정 run 크기(32)를 사용하는 간단한 버전입니다.

```python
def tim_sort_simplified(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
run_size = 32
for i in range(0, n, run_size):
    _insertion_sort_for_tim(result, i, min(i + run_size - 1, n - 1))
size = run_size
while size < n:
    for left in range(0, n, size * 2):
        mid = min(left + size - 1, n - 1)
        right = min(left + 2 * size - 1, n - 1)
        if mid < right:
            _merge_for_tim(result, left, mid, right)
    size *= 2
```
- `_calc_min_run` 대신 고정값 32를 사용합니다.
- 로직은 접근법 1과 동일하지만, 최적의 run 크기 계산을 생략합니다.
- 구현이 더 간단하고 이해하기 쉽습니다.

---

## 접근법 3: Python 내장 Tim Sort

Python의 `list.sort()`를 직접 사용합니다.

```python
def tim_sort_pythonic(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
result = arr[:]
result.sort()
return result
```
- Python의 `list.sort()`는 내부적으로 Tim Sort를 사용합니다.
- C로 구현되어 있어 순수 Python 구현보다 훨씬 빠릅니다.
- **실무에서는 이 방법을 사용**하는 것이 권장됩니다.
- `sorted(arr)`: 새 리스트를 반환하는 버전

### 실제 Tim Sort의 추가 최적화 (Python CPython 구현)

```
1. Natural run 탐지: 이미 정렬되거나 역순인 연속 구간을 자동으로 탐지
2. Galloping mode: 한쪽 배열의 원소가 연속으로 선택되면 이진 탐색으로 전환
3. Run 스택 관리: 병합 순서를 최적화하는 스택 기반 관리
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 (최선) | 시간 복잡도 (평균) | 시간 복잡도 (최악) | 공간 복잡도 |
|--------|-------------------|-------------------|-------------------|------------|
| Tim Sort 구현 | O(n) | O(n log n) | O(n log n) | O(n) |
| 단순화 Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) |
| Python 내장 sort() | O(n) | O(n log n) | O(n log n) | O(n) |

- **최선의 경우 O(n)**: 이미 정렬된 배열에서는 삽입 정렬이 O(n)에 완료되고, 병합이 필요 없습니다.
- Tim Sort는 실제 데이터에서 매우 효율적이며, 대부분의 프로그래밍 언어(Python, Java, JavaScript 등)에서 기본 정렬 알고리즘으로 채택되었습니다.
