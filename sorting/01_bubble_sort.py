"""
Sorting Algorithm Example 1: Bubble Sort
버블 정렬 - 인접한 두 원소를 비교하며 정렬하는 가장 기본적인 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
인접 원소를 반복적으로 비교·교환하여 큰 값을 뒤로 보낸다.
"""

from typing import List


def bubble_sort_basic(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 전체 패스를 n-1번 반복 (매 패스마다 가장 큰 값이 뒤로 이동)
    for i in range(n - 1):
        # 인접한 원소를 비교하며 끝에서 i개는 이미 정렬됨
        for j in range(n - 1 - i):
            # 현재 원소가 다음 원소보다 크면 교환
            if result[j] > result[j + 1]:
                # 두 원소의 위치를 교환 (스왑)
                result[j], result[j + 1] = result[j + 1], result[j]

    # 정렬된 배열을 반환
    return result


def bubble_sort_optimized(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 전체 패스를 n-1번 반복
    for i in range(n - 1):
        # 이번 패스에서 교환이 발생했는지 추적하는 플래그
        swapped = False

        # 인접한 원소를 비교
        for j in range(n - 1 - i):
            # 현재 원소가 다음 원소보다 크면 교환
            if result[j] > result[j + 1]:
                # 두 원소의 위치를 교환
                result[j], result[j + 1] = result[j + 1], result[j]
                # 교환이 발생했음을 기록
                swapped = True

        # 이번 패스에서 교환이 없었으면 이미 정렬 완료
        if not swapped:
            break

    # 정렬된 배열을 반환
    return result


def bubble_sort_recursive(arr: List[int], n: int = None) -> List[int]:
    # 최초 호출 시 복사본 생성 및 n 초기화
    if n is None:
        arr = arr[:]
        n = len(arr)

    # Base case: 배열 크기가 1이면 정렬 완료
    if n == 1:
        return arr

    # 한 번의 패스: 가장 큰 원소를 맨 뒤로 이동
    for i in range(n - 1):
        # 인접한 두 원소를 비교하여 교환
        if arr[i] > arr[i + 1]:
            # 현재 원소가 다음 원소보다 크면 스왑
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # 마지막 원소를 제외하고 재귀 호출 (이미 제자리에 있으므로)
    return bubble_sort_recursive(arr, n - 1)


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"원본 배열: {data}")

    # 기본 버블 정렬
    print(f"Basic:     {bubble_sort_basic(data)}")

    # 최적화된 버블 정렬 (조기 종료)
    print(f"Optimized: {bubble_sort_optimized(data)}")

    # 재귀 버블 정렬
    print(f"Recursive: {bubble_sort_recursive(data)}")

    # 이미 정렬된 배열 테스트 (최적화 버전이 빠르게 종료됨)
    sorted_data = [1, 2, 3, 4, 5]
    print(f"\n이미 정렬된 배열: {sorted_data}")
    print(f"Optimized: {bubble_sort_optimized(sorted_data)}")
