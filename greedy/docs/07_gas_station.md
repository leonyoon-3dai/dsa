# 07. Gas Station (주유소 문제)

## 문제 정의

원형으로 배치된 주유소가 있고, 각 주유소의 가스량과 다음 주유소까지의 비용이 주어진다. 시계 방향으로 한 바퀴 돌 수 있는 출발 주유소의 인덱스를 구하라. 불가능하면 -1을 반환. (LeetCode #134)

```
입력: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
출력: 3 (인덱스 3에서 출발하면 한 바퀴 가능)
```

---

## 접근법 1: 그리디 (한 번 순회)

전체 가스 >= 전체 비용이면 반드시 답이 존재한다는 성질을 이용한다.

```python
def gas_station_greedy(gas, cost) -> int:
```

### 라인별 설명

```python
total_gas = sum(gas)
total_cost = sum(cost)
if total_gas < total_cost:
    return -1
```
- **전체 가스 < 전체 비용**이면 어디서 출발해도 불가능하므로 -1 반환.
- 이 조건이 만족되면 **반드시 유일한 해가 존재**함이 증명되어 있습니다.

```python
start = 0
tank = 0
for i in range(len(gas)):
    tank += gas[i] - cost[i]
    if tank < 0:
        start = i + 1
        tank = 0
```
- 순회하면서 탱크에 가스를 넣고 비용을 뺍니다.
- 탱크가 음수가 되면 **현재까지의 모든 출발점이 불가능**합니다.
- 다음 주유소를 새 출발 후보로 설정하고 탱크를 초기화합니다.

**핵심 증명**: 만약 `start`에서 `i`까지 가다가 실패하면, `start`와 `i` 사이 어떤 점에서 출발해도 실패합니다. 왜냐하면 `start`에서 출발하면 중간 지점에 도착할 때 탱크가 0 이상이지만, 중간 지점에서 출발하면 0이기 때문입니다.

### 실행 예제

```
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

total_gas = 15, total_cost = 15 → 해 존재

i=0: tank = 0 + (1-3) = -2 < 0 → start=1, tank=0
i=1: tank = 0 + (2-4) = -2 < 0 → start=2, tank=0
i=2: tank = 0 + (3-5) = -2 < 0 → start=3, tank=0
i=3: tank = 0 + (4-1) = 3 >= 0 → 계속
i=4: tank = 3 + (5-2) = 6 >= 0 → 계속

결과: start = 3
```

---

## 접근법 2: 브루트포스

모든 출발점에서 시뮬레이션한다.

```python
def gas_station_brute_force(gas, cost) -> int:
```

### 라인별 설명

```python
for start in range(n):
    tank = 0
    success = True
    for j in range(n):
        idx = (start + j) % n
        tank += gas[idx] - cost[idx]
        if tank < 0:
            success = False
            break
    if success:
        return start
```
- 각 출발점에서 원형으로 한 바퀴 시뮬레이션합니다.
- `(start + j) % n`으로 원형 인덱스를 계산합니다.
- 중간에 탱크가 음수가 되면 실패, 한 바퀴를 돌면 성공.

### 실행 예제

```
start=0: tank: -2 → 실패
start=1: tank: -2 → 실패
start=2: tank: -2 → 실패
start=3: tank: 3→6→4→0→1 → 성공!

결과: 3
```

---

## 접근법 3: 경로 추적 포함

출발점을 찾고 각 지점에서의 탱크 잔량을 기록한다.

```python
def gas_station_with_trace(gas, cost) -> tuple[int, list[int]]:
```

### 라인별 설명

```python
for j in range(n):
    idx = (start + j) % n
    tank += gas[idx]
    tank_trace.append(tank)
    tank -= cost[idx]
```
- 출발점이 결정된 후, 경로를 따라가며 **충전 후 탱크 잔량**을 기록합니다.
- 디버깅이나 시각화에 유용합니다.

### 실행 예제

```
출발 인덱스: 3
경로: 3 → 4 → 0 → 1 → 2

충전 후 탱크: [4, 9, 7, 6, 6]
이동 후 탱크: [3, 7, 4, 2, 1]
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 그리디 (한 번 순회) | O(n) | O(1) |
| 브루트포스 | O(n^2) | O(1) |
| 경로 추적 포함 | O(n) | O(n) |
