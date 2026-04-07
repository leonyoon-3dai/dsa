# 09. Maximum Subarray (최대 부분 배열 합)

## 문제 정의

정수 배열 `nums`가 주어질 때, **합이 최대인 연속 부분 배열**을 찾고 그 합을 반환하라.

- Kadane's Algorithm 사용
- LeetCode #53

---

## 핵심 아이디어

각 위치에서 두 가지 선택:
1. 기존 부분 배열에 **이어붙이기**: `current_sum + nums[i]`
2. 현재 위치에서 **새로 시작**: `nums[i]`

**점화식**: `current_sum = max(nums[i], current_sum + nums[i])`

---

## 코드 라인별 설명

```python
current_sum = nums[0]
```
- 현재 위치에서 끝나는 부분 배열의 최대 합을 첫 번째 원소로 초기화합니다.

```python
max_sum = nums[0]
```
- 전체 최대 합도 첫 번째 원소로 초기화합니다.

```python
for i in range(1, len(nums)):
```
- 두 번째 원소(인덱스 1)부터 순회합니다.

```python
    current_sum = max(nums[i], current_sum + nums[i])
```
- **핵심 결정**: 두 가지 중 큰 값을 선택합니다:
  - `nums[i]`: 여기서 새로 시작 (이전 부분 배열이 음수여서 도움이 안 됨)
  - `current_sum + nums[i]`: 기존 부분 배열에 현재 원소를 추가

```python
    max_sum = max(max_sum, current_sum)
```
- 전체 최대 합을 갱신합니다.
- current_sum이 더 크면 max_sum을 업데이트합니다.

```python
return max_sum
```
- 전체 최대 합을 반환합니다.

---

## 실행 예제 1: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

```
i=0: current_sum = -2, max_sum = -2

i=1: current_sum = max(1, -2+1) = max(1, -1) = 1    ← 새로 시작
     max_sum = max(-2, 1) = 1

i=2: current_sum = max(-3, 1+(-3)) = max(-3, -2) = -2
     max_sum = max(1, -2) = 1

i=3: current_sum = max(4, -2+4) = max(4, 2) = 4    ← 새로 시작
     max_sum = max(1, 4) = 4

i=4: current_sum = max(-1, 4+(-1)) = max(-1, 3) = 3
     max_sum = max(4, 3) = 4

i=5: current_sum = max(2, 3+2) = 5
     max_sum = max(4, 5) = 5

i=6: current_sum = max(1, 5+1) = 6
     max_sum = max(5, 6) = 6       ← 최대값 갱신!

i=7: current_sum = max(-5, 6+(-5)) = max(-5, 1) = 1
     max_sum = max(6, 1) = 6

i=8: current_sum = max(4, 1+4) = 5
     max_sum = max(6, 5) = 6

결과: 6 (부분 배열 [4, -1, 2, 1])
```

## 실행 예제 2: nums = [5, 4, -1, 7, 8]

```
i=0: current=5, max=5
i=1: current=max(4, 5+4)=9, max=9
i=2: current=max(-1, 9-1)=8, max=9
i=3: current=max(7, 8+7)=15, max=15
i=4: current=max(8, 15+8)=23, max=23

결과: 23 (전체 배열이 최대 부분 배열)
```

## 실행 예제 3: nums = [-1, -2, -3]

```
i=0: current=-1, max=-1
i=1: current=max(-2, -1+(-2))=max(-2,-3)=-2, max=-1
i=2: current=max(-3, -2+(-3))=max(-3,-5)=-3, max=-1

결과: -1 (가장 큰 원소 하나)
모든 원소가 음수여도 정상 동작합니다.
```

---

## 복잡도

| 항목 | 값 |
|------|-----|
| 시간 복잡도 | O(n) - 한 번 순회 |
| 공간 복잡도 | O(1) - 변수 2개만 사용 |
