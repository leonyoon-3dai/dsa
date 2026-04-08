# 09. Assign Cookies (쿠키 배분)

## 문제 정의

아이들의 욕심 값 g[]와 쿠키 크기 s[]가 주어진다. 쿠키 크기가 아이의 욕심 값 이상이면 만족한다. 최대 몇 명의 아이를 만족시킬 수 있는가? (LeetCode #455)

```
입력: g = [1, 2, 3], s = [1, 1]
출력: 1 (크기 1 쿠키로 욕심 1인 아이만 만족 가능)

입력: g = [1, 2], s = [1, 2, 3]
출력: 2 (모든 아이 만족 가능)
```

---

## 접근법 1: 정방향 그리디 (작은 것부터)

욕심이 작은 아이에게 가장 작은 적합 쿠키를 배분한다.

```python
def assign_cookies_greedy(g: list[int], s: list[int]) -> int:
```

### 라인별 설명

```python
g_sorted = sorted(g)
s_sorted = sorted(s)
```
- 아이의 욕심 값과 쿠키 크기를 각각 **오름차순 정렬**합니다.
- 작은 것끼리 매칭하면 낭비가 최소화됩니다.

```python
child = 0
cookie = 0
while child < len(g_sorted) and cookie < len(s_sorted):
    if s_sorted[cookie] >= g_sorted[child]:
        child += 1
    cookie += 1
```
- **두 포인터** 기법을 사용합니다.
- 쿠키가 아이의 욕심을 만족시키면 `child`를 다음으로 이동 (만족한 아이 수 +1).
- 쿠키는 사용했든 작아서 못 줬든 항상 다음으로 이동합니다.

```python
return child
```
- `child` 포인터의 값이 곧 만족한 아이의 수입니다.

### 실행 예제

```
g = [1, 2, 3], s = [1, 1]
정렬: g = [1, 2, 3], s = [1, 1]

child=0, cookie=0: s[0]=1 >= g[0]=1 → 만족! child=1, cookie=1
child=1, cookie=1: s[1]=1 < g[1]=2 → 불만족. cookie=2
cookie=2 >= len(s) → 종료

결과: child = 1 (1명 만족)
```

---

## 접근법 2: 역방향 그리디 (큰 것부터)

욕심이 큰 아이에게 가장 큰 쿠키를 배분한다.

```python
def assign_cookies_reverse(g: list[int], s: list[int]) -> int:
```

### 라인별 설명

```python
g_sorted = sorted(g, reverse=True)
s_sorted = sorted(s, reverse=True)
```
- **내림차순** 정렬합니다.
- 큰 쿠키를 욕심 많은 아이에게 우선 배분합니다.

```python
cookie = 0
for child_greed in g_sorted:
    if cookie < len(s_sorted) and s_sorted[cookie] >= child_greed:
        count += 1
        cookie += 1
```
- 욕심이 큰 아이부터 순회합니다.
- 가장 큰 남은 쿠키가 욕심을 만족시키면 배분하고 다음 쿠키로 이동합니다.
- 만족 못 시키면 해당 아이를 건너뜁니다 (더 작은 쿠키로도 불가능하므로).

### 실행 예제

```
g = [1, 2], s = [1, 2, 3]
내림차순: g = [2, 1], s = [3, 2, 1]

greed=2: s[0]=3 >= 2 → 만족! count=1, cookie=1
greed=1: s[1]=2 >= 1 → 만족! count=2, cookie=2

결과: 2명 만족
```

---

## 접근법 3: 브루트포스 (최적 매칭)

각 아이에게 가장 적합한(가장 작은 적합) 쿠키를 찾아 배분한다.

```python
def assign_cookies_brute_force(g: list[int], s: list[int]) -> int:
```

### 라인별 설명

```python
for greed in sorted(g):
    best_cookie = -1
    best_size = float("inf")
    for j in range(len(s)):
        if not used[j] and s[j] >= greed:
            if s[j] < best_size:
                best_size = s[j]
                best_cookie = j
    if best_cookie != -1:
        used[best_cookie] = True
        count += 1
```
- 욕심이 작은 아이부터 순회합니다.
- 각 아이에 대해 사용하지 않은 쿠키 중 **욕심 이상이면서 가장 작은 쿠키**를 찾습니다.
- 이렇게 하면 큰 쿠키를 욕심 많은 아이를 위해 남겨둘 수 있습니다.

### 실행 예제

```
g = [1, 2, 3], s = [1, 1]

greed=1: 쿠키0(1) >= 1, 쿠키1(1) >= 1. best=0(크기1). 사용.
greed=2: 쿠키1(1) < 2. 적합 쿠키 없음.
greed=3: 적합 쿠키 없음.

결과: 1명 만족
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 정방향 그리디 | O(n log n + m log m) | O(n + m) 정렬 |
| 역방향 그리디 | O(n log n + m log m) | O(n + m) 정렬 |
| 브루트포스 | O(n * m) | O(m) used 배열 |

여기서 n = 아이 수, m = 쿠키 수.
