# 06. Heap Sort (힙 정렬)

## 문제 정의

주어진 배열을 오름차순으로 정렬하라.

```
배열을 최대 힙(Max Heap)으로 구성한 뒤,
루트(최댓값)를 꺼내어 배열 끝에 배치하는 과정을 반복한다.
```

항상 O(n log n)을 보장하며, 추가 메모리가 필요 없는 제자리 정렬이다.

---

## 접근법 1: 기본 힙 정렬

최대 힙을 구성한 후 루트를 추출하여 정렬합니다.

```python
def heap_sort_basic(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
for i in range(n // 2 - 1, -1, -1):
    _heapify(result, n, i)
```
- **Build Max Heap**: 마지막 비리프(non-leaf) 노드부터 루트까지 역순으로 heapify를 수행합니다.
- 마지막 비리프 노드의 인덱스: `n // 2 - 1`
- 리프 노드는 이미 힙 속성을 만족하므로 처리할 필요가 없습니다.

```python
for i in range(n - 1, 0, -1):
    result[0], result[i] = result[i], result[0]
    _heapify(result, i, 0)
```
- **정렬 단계**: 루트(최댓값)를 배열의 끝으로 이동하고, 힙 크기를 1 줄입니다.
- 루트와 마지막 원소를 교환한 후, 줄어든 힙에서 루트를 heapify합니다.
- 이 과정을 반복하면 배열이 오름차순으로 정렬됩니다.

**_heapify 함수:**

```python
def _heapify(arr, heap_size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _heapify(arr, heap_size, largest)
```
- `root`와 그 자식 노드 중 가장 큰 값을 찾습니다.
- 가장 큰 값이 `root`가 아니면 교환하고, 영향받은 서브트리에 대해 재귀적으로 heapify합니다.
- **배열에서의 힙 인덱스**: 노드 `i`의 왼쪽 자식은 `2i+1`, 오른쪽 자식은 `2i+2`

### 실행 예제: arr = [12, 11, 13, 5, 6, 7]

```
Build Max Heap:
  인덱스 2 (13): 이미 최대 → 변화 없음
  인덱스 1 (11): 자식 [5, 6] → 11이 최대 → 변화 없음
  인덱스 0 (12): 자식 [11, 13] → 13이 최대 → 교환
  → [13, 11, 12, 5, 6, 7]

정렬 단계:
  i=5: swap(13, 7) → [7, 11, 12, 5, 6, | 13]  heapify → [12, 11, 7, 5, 6, | 13]
  i=4: swap(12, 6) → [6, 11, 7, 5, | 12, 13]   heapify → [11, 6, 7, 5, | 12, 13]
  i=3: swap(11, 5) → [5, 6, 7, | 11, 12, 13]   heapify → [7, 6, 5, | 11, 12, 13]
  i=2: swap(7, 5)  → [5, 6, | 7, 11, 12, 13]   heapify → [6, 5, | 7, 11, 12, 13]
  i=1: swap(6, 5)  → [5, | 6, 7, 11, 12, 13]

결과: [5, 6, 7, 11, 12, 13]
```

---

## 접근법 2: Python heapq 모듈 활용

Python 표준 라이브러리의 최소 힙을 사용합니다.

```python
def heap_sort_pythonic(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
heap = arr[:]
heapq.heapify(heap)
result = []
while heap:
    result.append(heapq.heappop(heap))
```
- `heapq.heapify`: O(n) 시간에 배열을 최소 힙으로 변환합니다.
- `heapq.heappop`: O(log n) 시간에 최솟값을 꺼냅니다.
- **참고**: `heapq`는 최소 힙만 지원합니다. 최대 힙이 필요하면 값에 -1을 곱해야 합니다.

### 실행 예제: arr = [3, 1, 4, 1, 5]

```
heapify: [1, 1, 4, 3, 5]  (최소 힙)

heappop → 1: [1, 3, 4, 5]
heappop → 1: [3, 5, 4]
heappop → 3: [4, 5]
heappop → 4: [5]
heappop → 5: []

결과: [1, 1, 3, 4, 5]
```

---

## 접근법 3: 반복적 힙 정렬 (Iterative Heapify)

재귀 대신 반복문으로 heapify를 구현합니다.

```python
def heap_sort_iterative(arr: List[int]) -> List[int]:
```

### 라인별 설명

```python
def _heapify_iter(arr, heap_size, root):
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < heap_size and arr[left] > arr[largest]:
            largest = left
        if right < heap_size and arr[right] > arr[largest]:
            largest = right
        if largest == root:
            break
        arr[root], arr[largest] = arr[largest], arr[root]
        root = largest
```
- 재귀 호출 대신 `while` 루프를 사용합니다.
- `largest == root`이면 힙 속성이 만족되므로 종료합니다.
- 그렇지 않으면 교환 후 `root = largest`로 이동하여 다음 레벨을 검사합니다.
- **장점**: 호출 스택 오버헤드가 없어 큰 배열에서 더 효율적입니다.

---

## 복잡도 비교

| 접근법 | 시간 복잡도 (최선) | 시간 복잡도 (평균) | 시간 복잡도 (최악) | 공간 복잡도 |
|--------|-------------------|-------------------|-------------------|------------|
| 기본 힙 정렬 (재귀) | O(n log n) | O(n log n) | O(n log n) | O(log n) 호출 스택 |
| Python heapq | O(n log n) | O(n log n) | O(n log n) | O(n) 결과 배열 |
| 반복적 힙 정렬 | O(n log n) | O(n log n) | O(n log n) | O(1) |
