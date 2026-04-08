# 10. Task Scheduler (작업 스케줄러)

## 문제 정의

작업 배열 tasks와 쿨다운 시간 n이 주어진다. 같은 작업 사이에 최소 n 단위 시간의 간격이 필요하다. 모든 작업을 완료하는 데 필요한 최소 시간을 구하라. (LeetCode #621)

```
입력: tasks = ["A","A","A","B","B","B"], n = 2
출력: 8 (예: A B idle A B idle A B)
```

---

## 접근법 1: 그리디 (수학 공식)

가장 빈도가 높은 작업을 기준으로 프레임을 계산한다.

```python
def task_scheduler_greedy(tasks: list[str], n: int) -> int:
```

### 라인별 설명

```python
freq = Counter(tasks)
```
- 각 작업의 **빈도수**를 계산합니다. 예: `{'A': 3, 'B': 3}`.

```python
max_freq = max(freq.values())
```
- 가장 높은 빈도수를 구합니다. 예: 3.

```python
max_count = sum(1 for f in freq.values() if f == max_freq)
```
- **최대 빈도를 가진 작업의 개수**를 셉니다. 예: A와 B 모두 3이므로 2.

```python
result = (max_freq - 1) * (n + 1) + max_count
```
- **핵심 공식**:
  - `(max_freq - 1)`: 마지막 그룹을 제외한 **그룹 수**.
  - `(n + 1)`: 각 그룹의 크기 (작업 1개 + 쿨다운 n).
  - `max_count`: 마지막 그룹에 들어가는 작업 수.

```python
return max(result, len(tasks))
```
- 공식 결과가 전체 작업 수보다 작을 수 있습니다 (쿨다운 없이 빈틈없이 채울 수 있는 경우).
- 둘 중 큰 값이 정답입니다.

### 실행 예제

```
tasks = ["A","A","A","B","B","B"], n = 2

freq = {'A': 3, 'B': 3}
max_freq = 3
max_count = 2 (A와 B 모두 빈도 3)

result = (3-1) * (2+1) + 2 = 2 * 3 + 2 = 8

시각화:
  [A B _] [A B _] [A B]
   그룹1   그룹2   그룹3(마지막)

각 그룹 크기: n+1 = 3
그룹 수(마지막 제외): max_freq-1 = 2
마지막 그룹: max_count = 2 (A, B)

총: 2*3 + 2 = 8
```

**쿨다운이 충분히 작은 경우:**

```
tasks = ["A","A","A","B","B","B","C","C","D"], n = 1

freq = {'A': 3, 'B': 3, 'C': 2, 'D': 1}
max_freq = 3, max_count = 2

result = (3-1) * (1+1) + 2 = 6
len(tasks) = 9

max(6, 9) = 9  ← 쿨다운 없이도 9칸 필요

배치: A B C A B C A B D (9칸, idle 없음)
```

---

## 접근법 2: 시뮬레이션

실제로 스케줄을 구성하며 시간을 계산한다.

```python
def task_scheduler_simulation(tasks: list[str], n: int) -> int:
```

### 라인별 설명

```python
task_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
```
- 빈도 내림차순으로 정렬합니다.
- 빈도가 높은 작업을 먼저 배치하여 idle을 최소화합니다.

```python
while task_list:
    temp = []
    count = 0
    for i in range(n + 1):
        if i < len(task_list):
            task_name, task_freq = task_list[i]
            if task_freq > 1:
                temp.append((task_name, task_freq - 1))
            count += 1
```
- 한 라운드에 `n+1`개의 슬롯을 채웁니다.
- 빈도가 높은 작업부터 하나씩 배치합니다.
- 남은 횟수가 있으면 `temp`에 저장하여 다음 라운드에 사용합니다.

### 실행 예제

```
tasks = ["A","A","A","B","B","B"], n = 2

라운드 1: A(3), B(3) → [A, B, idle] → time=3
  남은: A(2), B(2)

라운드 2: A(2), B(2) → [A, B, idle] → time=6
  남은: A(1), B(1)

라운드 3: A(1), B(1) → [A, B] → time=8
  남은: 없음

총: 8
```

---

## 접근법 3: 공식 상세 설명

공식의 동작 원리를 설명 문자열과 함께 반환한다.

```python
def task_scheduler_formula_explained(tasks, n) -> tuple[int, str]:
```

### 라인별 설명

```python
frames = (max_freq - 1) * (n + 1) + max_count
explanation = (
    f"최대 빈도: {max_freq}, 최대 빈도 작업 수: {max_count}\n"
    f"프레임 계산: ({max_freq}-1) * ({n}+1) + {max_count} = {frames}\n"
    ...
)
return max(frames, total_tasks), explanation
```
- 공식의 각 요소를 한국어로 설명하는 문자열을 함께 반환합니다.
- 학습 및 디버깅 목적으로 유용합니다.

### 실행 예제

```
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2

최대 빈도: 6 (A)
최대 빈도 작업 수: 1 (A만)

프레임: (6-1) * (2+1) + 1 = 16
전체 작업 수: 12

max(16, 12) = 16

배치:
  A B C | A D E | A F G | A _ _ | A _ _ | A
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 그리디 (공식) | O(n) | O(1) (26개 문자) |
| 시뮬레이션 | O(총시간 * 26) | O(26) |
| 공식 + 설명 | O(n) | O(1) |
