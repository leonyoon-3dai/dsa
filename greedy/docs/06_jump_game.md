# 06. Jump Game (점프 게임)

## 문제 정의

정수 배열 nums가 주어지고, 각 원소는 해당 위치에서 점프할 수 있는 최대 거리이다. 인덱스 0에서 시작하여 마지막 인덱스에 도달할 수 있는지 판별하라. (LeetCode #55)

```
입력: nums = [2, 3, 1, 1, 4]
출력: True (0→1→4 또는 0→2→3→4)

입력: nums = [3, 2, 1, 0, 4]
출력: False (인덱스 3에서 막힘)
```

---

## 접근법 1: 정방향 그리디 (최대 도달 범위)

왼쪽에서 오른쪽으로 순회하며 도달 가능한 최대 인덱스를 갱신한다.

```python
def can_jump_greedy(nums: list[int]) -> bool:
```

### 라인별 설명

```python
max_reach = 0
```
- 현재까지 도달할 수 있는 **가장 먼 인덱스**를 0으로 초기화합니다.

```python
for i in range(len(nums)):
    if i > max_reach:
        return False
```
- 현재 인덱스 `i`가 `max_reach`를 넘으면, 이 위치에 도달할 수 없으므로 `False`.

```python
    max_reach = max(max_reach, i + nums[i])
    if max_reach >= len(nums) - 1:
        return True
```
- `i + nums[i]`: 현재 위치에서 최대로 갈 수 있는 인덱스.
- `max_reach`를 갱신하고, 마지막 인덱스에 도달 가능하면 즉시 `True`.

### 실행 예제

```
nums = [2, 3, 1, 1, 4], 마지막 인덱스 = 4

i=0: 0 <= 0 OK. max_reach = max(0, 0+2) = 2
i=1: 1 <= 2 OK. max_reach = max(2, 1+3) = 4. 4 >= 4 → True!

nums = [3, 2, 1, 0, 4], 마지막 인덱스 = 4

i=0: max_reach = max(0, 3) = 3
i=1: max_reach = max(3, 3) = 3
i=2: max_reach = max(3, 3) = 3
i=3: max_reach = max(3, 3) = 3
i=4: 4 > 3 → False!
```

---

## 접근법 2: 역방향 그리디

마지막에서 앞으로 역추적하며 목표 위치를 앞당긴다.

```python
def can_jump_backward(nums: list[int]) -> bool:
```

### 라인별 설명

```python
goal = n - 1
```
- 도달해야 할 **목표 위치**를 마지막 인덱스로 설정합니다.

```python
for i in range(n - 2, -1, -1):
    if i + nums[i] >= goal:
        goal = i
```
- 뒤에서 앞으로 순회합니다.
- 현재 위치에서 목표에 도달할 수 있으면, **목표를 현재 위치로 변경**합니다.
- 이 과정을 반복하면 목표가 점점 앞으로 이동합니다.

```python
return goal == 0
```
- 최종 목표가 0이면 시작점에서 끝까지 도달 가능합니다.

### 실행 예제

```
nums = [2, 3, 1, 1, 4], goal = 4

i=3: 3+1=4 >= 4 → goal=3
i=2: 2+1=3 >= 3 → goal=2
i=1: 1+3=4 >= 2 → goal=1
i=0: 0+2=2 >= 1 → goal=0

goal == 0 → True
```

---

## 접근법 3: 최소 점프 횟수 (Jump Game II)

마지막 인덱스에 도달하는 최소 점프 횟수를 구한다. (LeetCode #45)

```python
def min_jumps_greedy(nums: list[int]) -> int:
```

### 라인별 설명

```python
jumps = 0
current_end = 0
farthest = 0
```
- `jumps`: 현재까지의 점프 횟수.
- `current_end`: 현재 점프로 도달 가능한 최대 범위의 끝.
- `farthest`: 다음 점프에서 도달 가능한 최대 범위.

```python
for i in range(n - 1):
    farthest = max(farthest, i + nums[i])
    if i == current_end:
        jumps += 1
        current_end = farthest
        if current_end >= n - 1:
            break
```
- 각 위치에서 `farthest`를 갱신합니다.
- `current_end`에 도달하면 **한 번의 점프가 끝난 것**이므로 `jumps`를 증가시킵니다.
- `current_end`를 `farthest`로 갱신하여 다음 점프 범위를 설정합니다.

### 실행 예제

```
nums = [2, 3, 1, 1, 4]

i=0: farthest = max(0, 2) = 2. i==current_end(0) → jumps=1, current_end=2
i=1: farthest = max(2, 4) = 4. 
i=2: i==current_end(2) → jumps=2, current_end=4. 4>=4 → break

결과: 2번 점프 (0→1→4)
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 정방향 그리디 | O(n) | O(1) |
| 역방향 그리디 | O(n) | O(1) |
| 최소 점프 (그리디) | O(n) | O(1) |
