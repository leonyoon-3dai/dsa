# 04. Job Sequencing with Deadlines (작업 스케줄링)

## 문제 정의

각 작업에 마감일(deadline)과 이익(profit)이 주어진다. 한 번에 하나의 작업만 수행할 수 있고 각 작업은 1단위 시간이 걸린다. 마감일 전에 완료하면 이익을 얻는다. 최대 이익을 구하라.

```
입력: jobs = [("J1",2,100), ("J2",1,19), ("J3",2,27), ("J4",1,25), ("J5",3,15)]
출력: 총 이익 = 142, 선택 = [J1, J3, J5]
```

---

## 접근법 1: 그리디 (이익 기준 정렬)

이익이 큰 작업부터 가능한 가장 늦은 슬롯에 배치한다.

```python
def job_sequencing_greedy(jobs) -> tuple[int, list[str]]:
```

### 라인별 설명

```python
sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
```
- 이익(`x[2]`) 기준 **내림차순** 정렬합니다.
- 이익이 큰 작업을 먼저 배치하는 것이 그리디 전략입니다.

```python
max_deadline = max(job[1] for job in jobs)
slots = [None] * (max_deadline + 1)
```
- 최대 마감일만큼의 **시간 슬롯 배열**을 생성합니다.
- `slots[t] = None`이면 t 시점이 비어있음을 의미합니다.

```python
for job_id, deadline, profit in sorted_jobs:
    for t in range(deadline, 0, -1):
        if slots[t] is None:
            slots[t] = job_id
            total_profit += profit
            selected.append(job_id)
            break
```
- 각 작업에 대해 마감일부터 1까지 **역순으로** 빈 슬롯을 찾습니다.
- 가능한 **가장 늦은 시점**에 배치합니다 (앞의 슬롯을 다른 작업에 양보).
- 빈 슬롯을 찾으면 배치하고 다음 작업으로 넘어갑니다.

### 실행 예제

```
이익 내림차순 정렬: J1(100), J3(27), J4(25), J2(19), J5(15)
최대 마감일: 3
슬롯: [None, None, None, None]  (인덱스 0은 미사용)

1. J1(마감=2, 이익=100): 슬롯2 비어있음 → slots[2]=J1
   slots: [None, None, J1, None]

2. J3(마감=2, 이익=27): 슬롯2 사용중 → 슬롯1 비어있음 → slots[1]=J3
   slots: [None, J3, J1, None]

3. J4(마감=1, 이익=25): 슬롯1 사용중 → 빈 슬롯 없음 → 건너뜀

4. J2(마감=1, 이익=19): 슬롯1 사용중 → 빈 슬롯 없음 → 건너뜀

5. J5(마감=3, 이익=15): 슬롯3 비어있음 → slots[3]=J5
   slots: [None, J3, J1, J5]

총 이익: 100 + 27 + 15 = 142
```

---

## 접근법 2: Union-Find 최적화

슬롯 탐색을 Union-Find로 O(alpha(n))에 수행한다.

```python
def job_sequencing_with_union_find(jobs) -> tuple[int, list[str]]:
```

### 라인별 설명

```python
parent = list(range(max_deadline + 1))
```
- Union-Find의 `parent` 배열. 초기에는 각 슬롯이 자기 자신을 가리킵니다.

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
```
- **경로 압축**을 사용한 Find 연산입니다.
- `find(t)`는 t 이하에서 사용 가능한 가장 큰 슬롯을 반환합니다.

```python
available = find(deadline)
if available > 0:
    parent[available] = available - 1
    total_profit += profit
```
- `find(deadline)`으로 마감일 이하의 빈 슬롯을 빠르게 찾습니다.
- 슬롯을 사용하면 `parent[available] = available - 1`로 Union합니다.
- 이렇게 하면 다음 `find` 호출 시 이전 슬롯을 탐색하게 됩니다.

### 실행 예제

```
초기 parent: [0, 1, 2, 3]

1. J1(마감=2): find(2)=2 → 사용. parent[2]=1
   parent: [0, 1, 1, 3]

2. J3(마감=2): find(2)=find(1)=1 → 사용. parent[1]=0
   parent: [0, 0, 1, 3]

3. J4(마감=1): find(1)=find(0)=0 → 0은 유효하지 않음 → 건너뜀

4. J2(마감=1): find(1)=0 → 건너뜀

5. J5(마감=3): find(3)=3 → 사용. parent[3]=2
   parent: [0, 0, 1, 2]

총 이익: 100 + 27 + 15 = 142
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 그리디 (슬롯 탐색) | O(n^2) | O(n) |
| Union-Find 최적화 | O(n * alpha(n)) ≈ O(n) | O(n) |
