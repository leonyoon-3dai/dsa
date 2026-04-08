# 05. Minimum Platforms (최소 플랫폼 문제)

## 문제 정의

기차의 도착 시간과 출발 시간이 주어질 때, 모든 기차가 정차할 수 있도록 필요한 최소 플랫폼 수를 구하라.

```
입력: arrivals = [900, 940, 950, 1100, 1500, 1800]
      departures = [910, 1200, 1120, 1130, 1900, 2000]
출력: 3 (시간 950~1120 구간에서 최대 3대 동시 정차)
```

---

## 접근법 1: 정렬 + 두 포인터

도착과 출발을 별도로 정렬한 후, 두 포인터로 이벤트를 시간순 처리한다.

```python
def minimum_platforms_sorting(arrivals, departures) -> int:
```

### 라인별 설명

```python
arrivals_sorted = sorted(arrivals)
departures_sorted = sorted(departures)
```
- 도착 시간과 출발 시간을 **각각** 오름차순 정렬합니다.
- 별도 정렬해도 되는 이유: 특정 시점에 몇 대가 있는지만 중요하고, 어떤 기차인지는 상관없기 때문입니다.

```python
i = 0  # 도착 포인터
j = 0  # 출발 포인터
while i < n and j < n:
    if arrivals_sorted[i] <= departures_sorted[j]:
        platforms_needed += 1
        max_platforms = max(max_platforms, platforms_needed)
        i += 1
    else:
        platforms_needed -= 1
        j += 1
```
- 도착이 출발보다 빠르면(같으면) **플랫폼 추가** (도착 우선 처리).
- 출발이 빠르면 **플랫폼 해제**.
- `max_platforms`에 최대값을 기록합니다.

### 실행 예제

```
정렬 후:
  arrivals:   [900, 940, 950, 1100, 1500, 1800]
  departures: [910, 1120, 1130, 1200, 1900, 2000]

i=0, j=0: 900 <= 910 → 도착. platforms=1, max=1
i=1, j=0: 940 > 910  → 출발. platforms=0
i=1, j=1: 940 <= 1120 → 도착. platforms=1
i=2, j=1: 950 <= 1120 → 도착. platforms=2, max=2
i=3, j=1: 1100 <= 1120 → 도착. platforms=3, max=3
i=4, j=1: 1500 > 1120 → 출발. platforms=2
i=4, j=2: 1500 > 1130 → 출발. platforms=1
i=4, j=3: 1500 > 1200 → 출발. platforms=0
i=4, j=4: 1500 <= 1900 → 도착. platforms=1
i=5, j=4: 1800 <= 1900 → 도착. platforms=2
→ 종료

결과: max_platforms = 3
```

---

## 접근법 2: 이벤트 기반

모든 도착/출발을 하나의 이벤트 리스트로 합쳐서 처리한다.

```python
def minimum_platforms_event(arrivals, departures) -> int:
```

### 라인별 설명

```python
events = []
for t in arrivals:
    events.append((t, 1))      # 도착 = +1
for t in departures:
    events.append((t + 0.5, -1))  # 출발 = -1
```
- 도착은 `+1`, 출발은 `-1`로 표시합니다.
- 출발에 `+0.5`를 더해 같은 시간일 때 **도착이 먼저** 처리되게 합니다.

```python
events.sort()
for time, event_type in events:
    current += event_type
    max_platforms = max(max_platforms, current)
```
- 시간순으로 정렬 후 순회하며 `current`를 증감시킵니다.
- 최대값이 곧 최소 플랫폼 수입니다.

### 실행 예제

```
이벤트: [(900,+1), (910.5,-1), (940,+1), (950,+1), (1100,+1),
         (1120.5,-1), (1130.5,-1), (1200.5,-1), (1500,+1), (1800,+1),
         (1900.5,-1), (2000.5,-1)]

시간순 처리:
  900: +1 → current=1
  910.5: -1 → current=0
  940: +1 → current=1
  950: +1 → current=2
  1100: +1 → current=3  ← 최대!
  1120.5: -1 → current=2
  ...

결과: 3
```

---

## 접근법 3: 브루트포스

각 도착 시점에서 동시에 정차 중인 기차 수를 모두 확인한다.

```python
def minimum_platforms_brute_force(arrivals, departures) -> int:
```

### 라인별 설명

```python
for i in range(n):
    count = 0
    for j in range(n):
        if arrivals[j] <= arrivals[i] and departures[j] >= arrivals[i]:
            count += 1
    max_platforms = max(max_platforms, count)
```
- 각 도착 시점 `arrivals[i]`에 대해, 해당 시점에 정차 중인 기차를 모두 셉니다.
- j번 기차가 정차 중인 조건: `arrivals[j] <= arrivals[i] <= departures[j]`.
- 모든 시점의 최대값이 답입니다.

### 실행 예제

```
i=0 (t=900):  J0(900~910) → 1대
i=1 (t=940):  J1(940~1200) → 1대
i=2 (t=950):  J1(940~1200), J2(950~1120) → 2대
i=3 (t=1100): J1(940~1200), J2(950~1120), J3(1100~1130) → 3대
...

결과: 3
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 정렬 + 두 포인터 | O(n log n) | O(n) |
| 이벤트 기반 | O(n log n) | O(n) |
| 브루트포스 | O(n^2) | O(1) |
