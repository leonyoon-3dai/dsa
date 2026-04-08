# 07. Counting Sort (계수 정렬)

## 문제 정의

주어진 배열을 오름차순으로 정렬하라.

```
각 원소의 등장 횟수를 세고(count),
누적합을 이용하여 각 원소의 최종 위치를 결정한다.
```

비교 기반이 아닌 정렬로, 값의 범위가 작을 때 O(n+k) 시간에 정렬한다. (k = 값의 범위)

---

## 접근법 1: 기본 계수 정렬

등장 횟수를 세고, 횟수만큼 결과에 추가합니다.

```python
def counting_sort_basic(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
if not arr:
    return []
max_val = max(arr)
min_val = min(arr)
range_val = max_val - min_val + 1
```
- 빈 배열이면 빈 리스트를 반환합니다.
- 최댓값과 최솟값을 구하여 값의 범위를 계산합니다.
- `range_val`: 카운트 배열의 크기입니다.

```python
count = [0] * range_val
for num in arr:
    count[num - min_val] += 1
```
- 카운트 배열을 0으로 초기화합니다.
- 각 원소에 대해 `num - min_val` 인덱스의 카운트를 증가시킵니다.
- `min_val`을 빼서 음수도 처리할 수 있도록 합니다.

```python
result = []
for i in range(range_val):
    result.extend([i + min_val] * count[i])
```
- 카운트 배열을 순회하며, 각 값을 등장 횟수만큼 결과에 추가합니다.
- `i + min_val`: 원래 값으로 복원합니다.

### 실행 예제: arr = [4, 2, 2, 8, 3, 3, 1]

```
min_val=1, max_val=8, range_val=8

카운팅:
  count[0] (값 1): 1
  count[1] (값 2): 2
  count[2] (값 3): 2
  count[3] (값 4): 1
  count[4~6] (값 5~7): 0
  count[7] (값 8): 1
  → count = [1, 2, 2, 1, 0, 0, 0, 1]

결과 생성:
  i=0: [1]
  i=1: [1, 2, 2]
  i=2: [1, 2, 2, 3, 3]
  i=3: [1, 2, 2, 3, 3, 4]
  i=7: [1, 2, 2, 3, 3, 4, 8]

결과: [1, 2, 2, 3, 3, 4, 8]
```

---

## 접근법 2: 안정 계수 정렬

누적합을 사용하여 안정 정렬(stable sort)을 보장합니다.

```python
def counting_sort_stable(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
count = [0] * range_val
for num in arr:
    count[num - min_val] += 1
```
- 각 원소의 등장 횟수를 카운트합니다. (접근법 1과 동일)

```python
for i in range(1, range_val):
    count[i] += count[i - 1]
```
- **누적합 계산**: `count[i]`는 값이 `i + min_val` **이하**인 원소의 총 개수를 나타냅니다.
- 이 누적합이 각 원소의 최종 위치를 결정하는 핵심입니다.

```python
result = [0] * len(arr)
for i in range(len(arr) - 1, -1, -1):
    idx = arr[i] - min_val
    count[idx] -= 1
    result[count[idx]] = arr[i]
```
- **뒤에서부터 순회**: 같은 값의 원소들 중 뒤에 있는 것이 결과에서도 뒤에 오도록 보장합니다.
- `count[idx] -= 1`: 누적합을 1 감소시켜 다음 같은 값의 위치를 지정합니다.
- 이렇게 하면 **안정 정렬**이 보장됩니다.

### 실행 예제: arr = [4, 2, 2, 8, 3, 3, 1]

```
카운트: [1, 2, 2, 1, 0, 0, 0, 1]
누적합: [1, 3, 5, 6, 6, 6, 6, 7]

뒤에서부터 배치 (안정 정렬):
  i=6, arr[6]=1: count[0]=1→0, result[0]=1
  i=5, arr[5]=3: count[2]=5→4, result[4]=3
  i=4, arr[4]=3: count[2]=4→3, result[3]=3
  i=3, arr[3]=8: count[7]=7→6, result[6]=8
  i=2, arr[2]=2: count[1]=3→2, result[2]=2
  i=1, arr[1]=2: count[1]=2→1, result[1]=2
  i=0, arr[0]=4: count[3]=6→5, result[5]=4

결과: [1, 2, 2, 3, 3, 4, 8]
```

---

## 접근법 3: 기수 정렬용 계수 정렬

특정 자릿수를 기준으로 계수 정렬을 수행합니다. (기수 정렬의 서브루틴)

```python
def counting_sort_for_radix(arr: List[int], exp: int) -> List[int]:
```

### 라인별 설명

```python
digit = (num // exp) % 10
count[digit] += 1
```
- `exp` 자릿수의 숫자를 추출합니다.
  - `exp=1`: 일의 자리
  - `exp=10`: 십의 자리
  - `exp=100`: 백의 자리
- 해당 자릿수 숫자(0~9)의 등장 횟수를 카운트합니다.

```python
for i in range(1, 10):
    count[i] += count[i - 1]
```
- 0~9에 대한 누적합을 계산합니다.

```python
for i in range(n - 1, -1, -1):
    digit = (arr[i] // exp) % 10
    count[digit] -= 1
    result[count[digit]] = arr[i]
```
- 뒤에서부터 순회하여 안정 정렬을 보장합니다.
- 이 함수는 기수 정렬(`08_radix_sort.py`)에서 각 자릿수별로 호출됩니다.

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 | 안정 정렬 |
|--------|------------|------------|----------|
| 기본 계수 정렬 | O(n + k) | O(k) | 아니오 |
| 안정 계수 정렬 | O(n + k) | O(n + k) | 예 |
| 기수 정렬용 | O(n + 10) = O(n) | O(n + 10) = O(n) | 예 |

- `n`: 배열의 크기, `k`: 값의 범위 (max - min + 1)
- `k`가 `n`에 비해 매우 크면 비효율적이므로, 값의 범위가 제한된 경우에 사용합니다.
