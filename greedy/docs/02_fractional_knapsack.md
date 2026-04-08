# 02. Fractional Knapsack (분할 가능 배낭 문제)

## 문제 정의

각 물건의 무게와 가치가 주어질 때, 배낭의 용량 W를 초과하지 않으면서 최대 가치를 얻어라. 물건을 쪼개서 일부만 담을 수 있다.

```
입력: weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
출력: 240.0
설명: 물건0 전체(60) + 물건1 전체(100) + 물건2의 2/3(80) = 240
```

---

## 접근법 1: 그리디 (단위 무게당 가치 정렬)

단위 무게당 가치(value/weight)가 높은 물건부터 담는다.

```python
def fractional_knapsack_greedy(weights, values, capacity) -> float:
```

### 라인별 설명

```python
items = []
for i in range(n):
    ratio = values[i] / weights[i]
    items.append((ratio, weights[i], values[i]))
```
- 각 물건의 **단위 무게당 가치**(ratio)를 계산합니다.
- `(비율, 무게, 가치)` 튜플로 저장합니다.

```python
items.sort(key=lambda x: x[0], reverse=True)
```
- 비율 기준 **내림차순** 정렬합니다.
- 가치 효율이 높은 물건을 먼저 담기 위함입니다.

```python
for ratio, weight, value in items:
    if remaining <= 0:
        break
    if weight <= remaining:
        total_value += value
        remaining -= weight
    else:
        total_value += ratio * remaining
        remaining = 0
```
- 물건 전체를 담을 수 있으면 전부 담습니다.
- 담을 수 없으면 **남은 용량만큼만 비율적으로** 담습니다.
- 이것이 0/1 배낭 문제와의 핵심 차이점입니다.

### 실행 예제

```
물건 비율 계산:
  물건0: 60/10 = 6.0
  물건1: 100/20 = 5.0
  물건2: 120/30 = 4.0

비율 내림차순 정렬: 물건0(6.0), 물건1(5.0), 물건2(4.0)
용량: 50

1. 물건0: 무게=10, 용량충분 → 전부 담음. 가치+=60, 남은용량=40
2. 물건1: 무게=20, 용량충분 → 전부 담음. 가치+=100, 남은용량=20
3. 물건2: 무게=30 > 남은용량=20 → 20/30만 담음. 가치+=4.0*20=80

총 가치: 60 + 100 + 80 = 240.0
```

---

## 접근법 2: 상세 결과 포함 그리디

어떤 물건을 얼마나 담았는지 추적하는 버전.

```python
def fractional_knapsack_with_detail(weights, values, capacity) -> tuple[float, list]:
```

### 라인별 설명

```python
indexed_items = []
for i in range(n):
    ratio = values[i] / weights[i]
    indexed_items.append((ratio, i))
```
- 원본 인덱스를 함께 저장하여, 결과에서 어떤 물건인지 추적합니다.

```python
take_weight = min(weights[idx], remaining)
take_value = ratio * take_weight
fraction = take_weight / weights[idx]
taken.append((idx, fraction))
```
- `take_weight`: 실제로 담을 수 있는 무게 (전체 또는 남은 용량).
- `fraction`: 담은 비율 (0.0 ~ 1.0). 1.0이면 전체를 담은 것.
- 결과에 `(물건 인덱스, 담은 비율)`을 기록합니다.

### 실행 예제

```
결과:
  물건 0: 무게=10, 가치=60, 담은 비율=1.00 (100%)
  물건 1: 무게=20, 가치=100, 담은 비율=1.00 (100%)
  물건 2: 무게=30, 가치=120, 담은 비율=0.67 (67%)

총 가치: 240.0
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 그리디 (비율 정렬) | O(n log n) | O(n) |
| 상세 결과 포함 | O(n log n) | O(n) |
| 참고: 0/1 배낭 (DP) | O(nW) | O(nW) |

**그리디가 최적해를 보장하는 이유**: 물건을 분할할 수 있으므로, 단위 가치가 높은 물건을 우선 담는 것이 항상 최적입니다.
