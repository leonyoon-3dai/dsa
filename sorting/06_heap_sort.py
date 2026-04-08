"""
Sorting Algorithm Example 6: Heap Sort
힙 정렬 - 최대 힙 자료구조를 이용한 비교 기반 정렬 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
배열을 최대 힙으로 구성한 뒤, 루트(최댓값)를 꺼내어 정렬한다.
"""

from typing import List
import heapq


def heap_sort_basic(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 최대 힙 구성 (Build Max Heap)
    # 마지막 비리프 노드부터 루트까지 역순으로 heapify 수행
    for i in range(n // 2 - 1, -1, -1):
        # 각 노드에 대해 최대 힙 속성을 복원
        _heapify(result, n, i)

    # 힙에서 원소를 하나씩 추출하여 정렬
    for i in range(n - 1, 0, -1):
        # 루트(최댓값)를 배열의 끝으로 이동
        result[0], result[i] = result[i], result[0]

        # 줄어든 힙에 대해 루트부터 heapify 수행
        _heapify(result, i, 0)

    # 정렬된 배열을 반환
    return result


def _heapify(arr: List[int], heap_size: int, root: int) -> None:
    # 현재 노드를 가장 큰 값으로 가정
    largest = root

    # 왼쪽 자식 노드의 인덱스
    left = 2 * root + 1

    # 오른쪽 자식 노드의 인덱스
    right = 2 * root + 2

    # 왼쪽 자식이 현재 노드보다 크면 largest 갱신
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재 largest보다 크면 largest 갱신
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # largest가 root가 아니면 교환하고 재귀적으로 heapify
    if largest != root:
        # 루트와 가장 큰 자식을 교환
        arr[root], arr[largest] = arr[largest], arr[root]
        # 영향받은 서브트리에 대해 재귀적으로 heapify
        _heapify(arr, heap_size, largest)


def heap_sort_pythonic(arr: List[int]) -> List[int]:
    # Python의 heapq 모듈은 최소 힙을 제공
    # 배열을 최소 힙으로 변환
    heap = arr[:]
    heapq.heapify(heap)

    # 힙에서 원소를 하나씩 꺼내어 정렬된 배열 생성
    result = []
    while heap:
        # 최솟값을 꺼내어 결과 배열에 추가
        result.append(heapq.heappop(heap))

    # 정렬된 배열을 반환
    return result


def heap_sort_iterative(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 반복적(iterative) heapify 함수
    def _heapify_iter(arr: List[int], heap_size: int, root: int) -> None:
        while True:
            # 현재 노드를 가장 큰 값으로 가정
            largest = root

            # 왼쪽 자식 노드 인덱스
            left = 2 * root + 1

            # 오른쪽 자식 노드 인덱스
            right = 2 * root + 2

            # 왼쪽 자식이 현재 노드보다 크면 largest 갱신
            if left < heap_size and arr[left] > arr[largest]:
                largest = left

            # 오른쪽 자식이 현재 largest보다 크면 largest 갱신
            if right < heap_size and arr[right] > arr[largest]:
                largest = right

            # largest가 root와 같으면 힙 속성 만족, 종료
            if largest == root:
                break

            # 교환하고 다음 레벨로 이동
            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        _heapify_iter(result, n, i)

    # 힙에서 원소를 하나씩 추출하여 정렬
    for i in range(n - 1, 0, -1):
        # 루트(최댓값)를 배열의 끝으로 이동
        result[0], result[i] = result[i], result[0]
        # 줄어든 힙에 대해 heapify
        _heapify_iter(result, i, 0)

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [12, 11, 13, 5, 6, 7]
    print(f"원본 배열: {data}")

    # 기본 힙 정렬
    print(f"Basic:     {heap_sort_basic(data)}")

    # Python heapq 모듈 활용
    print(f"Pythonic:  {heap_sort_pythonic(data)}")

    # 반복적 힙 정렬
    print(f"Iterative: {heap_sort_iterative(data)}")

    # 큰 배열 테스트
    import random
    large_data = random.sample(range(100), 15)
    print(f"\n랜덤 배열: {large_data}")
    print(f"정렬 결과: {heap_sort_basic(large_data)}")
