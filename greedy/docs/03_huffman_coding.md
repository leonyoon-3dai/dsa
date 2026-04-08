# 03. Huffman Coding (허프만 코딩)

## 문제 정의

문자와 빈도수가 주어질 때, 최적의 이진 접두어 코드를 생성하라. 빈도가 높은 문자에 짧은 코드를 할당하여 전체 인코딩 길이를 최소화한다.

```
입력: {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
출력: f→0, c→100, d→101, a→1100, b→1101, e→111 (예시, 트리 구조에 따라 다를 수 있음)
```

---

## 접근법 1: 허프만 트리 구성 (최소 힙)

빈도가 가장 낮은 두 노드를 반복적으로 합쳐서 트리를 구성한다.

```python
def huffman_coding(char_freq: dict[str, int]) -> dict[str, str]:
```

### 라인별 설명

```python
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
```
- 허프만 트리의 **노드 클래스**입니다.
- `char`: 문자 (내부 노드는 `None`).
- `freq`: 빈도수.
- `left`, `right`: 자식 노드.

```python
def __lt__(self, other):
    return self.freq < other.freq
```
- 힙(우선순위 큐)에서 **비교 연산**을 위해 정의합니다.
- 빈도수가 낮은 것이 우선순위가 높습니다.

```python
for char, freq in char_freq.items():
    node = HuffmanNode(char, freq)
    heapq.heappush(heap, node)
```
- 각 문자를 **리프 노드**로 만들어 최소 힙에 삽입합니다.

```python
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    merged = HuffmanNode(None, left.freq + right.freq)
    merged.left = left
    merged.right = right
    heapq.heappush(heap, merged)
```
- **핵심 그리디 단계**: 빈도가 가장 낮은 두 노드를 꺼내서 합칩니다.
- 합친 노드의 빈도는 두 노드 빈도의 합입니다.
- 새 노드를 다시 힙에 넣습니다.
- 노드가 1개 남을 때까지 반복하면 허프만 트리가 완성됩니다.

```python
def build_codes(node, current_code):
    if node.char is not None:
        codes[node.char] = current_code if current_code else "0"
        return
    build_codes(node.left, current_code + "0")
    build_codes(node.right, current_code + "1")
```
- 트리를 DFS로 순회하며 코드를 생성합니다.
- **왼쪽**으로 가면 `"0"`, **오른쪽**으로 가면 `"1"`을 추가합니다.
- 리프 노드에 도달하면 해당 문자의 코드를 저장합니다.

### 실행 예제

```
초기 힙: a(5), b(9), c(12), d(13), e(16), f(45)

1단계: a(5) + b(9) = ab(14)
  힙: c(12), d(13), ab(14), e(16), f(45)

2단계: c(12) + d(13) = cd(25)
  힙: ab(14), e(16), cd(25), f(45)

3단계: ab(14) + e(16) = abe(30)
  힙: cd(25), abe(30), f(45)

4단계: cd(25) + abe(30) = cdabe(55)
  힙: f(45), cdabe(55)

5단계: f(45) + cdabe(55) = root(100)

코드 생성 (트리 순회):
  f → 0       (1비트)
  c → 100     (3비트)
  d → 101     (3비트)
  a → 1100    (4비트)
  b → 1101    (4비트)
  e → 111     (3비트)
```

---

## 접근법 2: 인코딩 / 디코딩

생성된 코드로 문자열을 인코딩하고 디코딩한다.

```python
def huffman_encode(text, codes) -> str:
def huffman_decode(encoded, char_freq) -> str:
```

### 라인별 설명

**인코딩:**
```python
for char in text:
    encoded += codes[char]
```
- 각 문자를 허프만 코드로 변환하여 이어 붙입니다.

**디코딩:**
```python
for bit in encoded:
    if bit == "0":
        current = current.left
    else:
        current = current.right
    if current.char is not None:
        decoded += current.char
        current = root
```
- 비트를 하나씩 읽으며 트리를 탐색합니다.
- 리프에 도달하면 문자를 추가하고 루트로 돌아갑니다.
- **접두어 코드**이므로 모호함 없이 디코딩 가능합니다.

### 실행 예제

```
원본: "abcdef"
인코딩: "1100" + "1101" + "100" + "101" + "111" + "0"
      = "110011011001011110"  (18비트)

고정 길이 코드라면: 6문자 × 3비트 = 18비트
허프만 코딩의 장점: 빈도가 높은 'f'는 1비트만 사용
```

---

## 복잡도 비교

| 접근법 | 시간 복잡도 | 공간 복잡도 |
|--------|------------|------------|
| 허프만 트리 구성 | O(n log n) | O(n) |
| 인코딩 | O(m) (m=텍스트 길이) | O(m) |
| 디코딩 | O(k) (k=비트 수) | O(n) 트리 |
