"""
Greedy Example 3: Huffman Coding (허프만 코딩)

Problem: 문자와 빈도수가 주어질 때, 최적의 이진 접두어 코드를 생성하라.
         빈도가 높은 문자에 짧은 코드를 할당하여 전체 인코딩 길이를 최소화한다.
"""

import heapq


class HuffmanNode:
    # 허프만 트리의 노드 클래스
    def __init__(self, char: str, freq: int):
        # 문자 (내부 노드는 None)
        self.char = char
        # 빈도수
        self.freq = freq
        # 왼쪽 자식 노드
        self.left = None
        # 오른쪽 자식 노드
        self.right = None

    # 힙 비교를 위한 less-than 연산자 정의
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(char_freq: dict[str, int]) -> dict[str, str]:
    # 최소 힙 (우선순위 큐) 생성
    heap = []

    # 각 문자에 대해 노드를 생성하고 힙에 삽입
    for char, freq in char_freq.items():
        # 리프 노드 생성
        node = HuffmanNode(char, freq)
        # 힙에 추가
        heapq.heappush(heap, node)

    # 노드가 1개 남을 때까지 반복 (트리 구성)
    while len(heap) > 1:
        # 빈도가 가장 낮은 두 노드를 꺼냄
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # 두 노드의 빈도 합으로 새 내부 노드 생성
        merged = HuffmanNode(None, left.freq + right.freq)
        # 왼쪽 자식 설정
        merged.left = left
        # 오른쪽 자식 설정
        merged.right = right

        # 새 노드를 힙에 삽입
        heapq.heappush(heap, merged)

    # 루트 노드
    root = heap[0]

    # 코드 테이블을 저장할 딕셔너리
    codes = {}

    def build_codes(node: HuffmanNode, current_code: str):
        # 노드가 None이면 반환
        if node is None:
            return

        # 리프 노드이면 코드를 저장
        if node.char is not None:
            # 문자가 하나뿐인 특수 경우 처리
            codes[node.char] = current_code if current_code else "0"
            return

        # 왼쪽으로 가면 '0' 추가
        build_codes(node.left, current_code + "0")
        # 오른쪽으로 가면 '1' 추가
        build_codes(node.right, current_code + "1")

    # 루트부터 코드 생성 시작
    build_codes(root, "")

    # 코드 테이블 반환
    return codes


def huffman_encode(text: str, codes: dict[str, str]) -> str:
    # 각 문자를 해당 허프만 코드로 변환하여 이어 붙임
    encoded = ""
    for char in text:
        # 문자에 해당하는 코드를 추가
        encoded += codes[char]
    # 인코딩된 비트 문자열 반환
    return encoded


def huffman_decode(encoded: str, char_freq: dict[str, int]) -> str:
    # 디코딩을 위해 허프만 트리를 다시 구성
    heap = []
    for char, freq in char_freq.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # 루트 노드
    root = heap[0]
    # 디코딩 결과 문자열
    decoded = ""
    # 현재 탐색 중인 노드
    current = root

    # 인코딩된 비트를 하나씩 순회
    for bit in encoded:
        # '0'이면 왼쪽으로 이동
        if bit == "0":
            current = current.left
        # '1'이면 오른쪽으로 이동
        else:
            current = current.right

        # 리프 노드에 도달하면 문자를 추가
        if current.char is not None:
            decoded += current.char
            # 루트로 돌아가서 다음 문자 탐색
            current = root

    # 디코딩된 문자열 반환
    return decoded


# === 실행 예제 ===
if __name__ == "__main__":
    # 문자별 빈도수
    char_freq = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}

    print("문자 빈도수:", char_freq)
    print()

    # 허프만 코드 생성
    codes = huffman_coding(char_freq)
    print("허프만 코드:")
    for char in sorted(codes.keys()):
        print(f"  '{char}': {codes[char]}")

    # 인코딩 예시
    text = "abcdef"
    encoded = huffman_encode(text, codes)
    print(f"\n원본: '{text}'")
    print(f"인코딩: {encoded}")
    print(f"인코딩 길이: {len(encoded)} bits")

    # 디코딩 예시
    decoded = huffman_decode(encoded, char_freq)
    print(f"디코딩: '{decoded}'")
    print(f"원본과 일치: {text == decoded}")
