"""
Sorting Algorithm Example 3: Insertion Sort
삽입 정렬 - 원소를 하나씩 올바른 위치에 삽입하여 정렬하는 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
카드를 정리하듯이, 각 원소를 이미 정렬된 부분의 올바른 위치에 삽입한다.
"""

from typing import List
import bisect


def insertion_sort_basic(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 인덱스 1부터 시작 (첫 번째 원소는 이미 정렬된 것으로 간주)
    for i in range(1, n):
        # 현재 삽입할 원소를 key에 저장
        key = result[i]

        # 정렬된 부분의 마지막 인덱스
        j = i - 1

        # key보다 큰 원소들을 오른쪽으로 한 칸씩 이동
        while j >= 0 and result[j] > key:
            # 원소를 한 칸 오른쪽으로 이동
            result[j + 1] = result[j]
            # 비교 위치를 왼쪽으로 이동
            j -= 1

        # key를 올바른 위치에 삽입
        result[j + 1] = key

    # 정렬된 배열을 반환
    return result


def insertion_sort_recursive(arr: List[int], n: int = None) -> List[int]:
    # 최초 호출 시 복사본 생성 및 n 초기화
    if n is None:
        arr = arr[:]
        n = len(arr)

    # Base case: 크기가 1 이하이면 정렬 완료
    if n <= 1:
        return arr

    # 앞의 n-1개 원소를 먼저 재귀적으로 정렬
    insertion_sort_recursive(arr, n - 1)

    # n번째 원소(인덱스 n-1)를 올바른 위치에 삽입
    key = arr[n - 1]

    # 정렬된 부분의 마지막 인덱스
    j = n - 2

    # key보다 큰 원소들을 오른쪽으로 이동
    while j >= 0 and arr[j] > key:
        # 원소를 한 칸 오른쪽으로 이동
        arr[j + 1] = arr[j]
        # 비교 위치를 왼쪽으로 이동
        j -= 1

    # key를 올바른 위치에 삽입
    arr[j + 1] = key

    # 정렬된 배열을 반환
    return arr


def insertion_sort_binary_search(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 인덱스 1부터 시작
    for i in range(1, n):
        # 현재 삽입할 원소를 key에 저장
        key = result[i]

        # 이진 탐색으로 삽입 위치를 찾음 (비교 횟수 O(log i))
        pos = bisect.bisect_left(result, key, 0, i)

        # 삽입 위치부터 현재 위치까지 원소를 한 칸씩 오른쪽으로 이동
        for j in range(i, pos, -1):
            result[j] = result[j - 1]

        # key를 찾은 위치에 삽입
        result[pos] = key

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [12, 11, 13, 5, 6]
    print(f"원본 배열: {data}")

    # 기본 삽입 정렬
    print(f"Basic:         {insertion_sort_basic(data)}")

    # 재귀 삽입 정렬
    print(f"Recursive:     {insertion_sort_recursive(data)}")

    # 이진 탐색 삽입 정렬
    print(f"Binary Search: {insertion_sort_binary_search(data)}")

    # 거의 정렬된 배열 테스트 (삽입 정렬에 유리)
    nearly_sorted = [1, 2, 4, 3, 5, 6, 8, 7]
    print(f"\n거의 정렬된 배열: {nearly_sorted}")
    print(f"Basic:         {insertion_sort_basic(nearly_sorted)}")
