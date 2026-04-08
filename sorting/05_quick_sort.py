"""
Sorting Algorithm Example 5: Quick Sort
퀵 정렬 - 피벗을 기준으로 분할하여 정렬하는 분할 정복 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
피벗 원소를 선택하고, 피벗보다 작은 것과 큰 것으로 분할한 뒤 재귀적으로 정렬한다.
"""

from typing import List
import random


def quick_sort_lomuto(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 내부 재귀 함수 정의 (Lomuto 파티션)
    def _sort(arr: List[int], low: int, high: int) -> None:
        # Base case: 구간의 크기가 1 이하이면 반환
        if low >= high:
            return

        # Lomuto 파티션 수행하여 피벗의 최종 위치를 얻음
        pivot_idx = _partition_lomuto(arr, low, high)

        # 피벗 왼쪽 구간을 재귀적으로 정렬
        _sort(arr, low, pivot_idx - 1)

        # 피벗 오른쪽 구간을 재귀적으로 정렬
        _sort(arr, pivot_idx + 1, high)

    def _partition_lomuto(arr: List[int], low: int, high: int) -> int:
        # 마지막 원소를 피벗으로 선택
        pivot = arr[high]

        # i는 피벗보다 작은 원소들의 경계를 가리킴
        i = low - 1

        # low부터 high-1까지 순회
        for j in range(low, high):
            # 현재 원소가 피벗보다 작거나 같으면
            if arr[j] <= pivot:
                # 경계를 오른쪽으로 이동
                i += 1
                # 현재 원소를 경계 위치로 교환
                arr[i], arr[j] = arr[j], arr[i]

        # 피벗을 경계 바로 오른쪽에 배치
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # 피벗의 최종 위치를 반환
        return i + 1

    # 전체 배열에 대해 정렬 수행
    _sort(result, 0, len(result) - 1)

    # 정렬된 배열을 반환
    return result


def quick_sort_hoare(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 내부 재귀 함수 정의 (Hoare 파티션)
    def _sort(arr: List[int], low: int, high: int) -> None:
        # Base case: 구간의 크기가 1 이하이면 반환
        if low >= high:
            return

        # Hoare 파티션 수행하여 분할 지점을 얻음
        p = _partition_hoare(arr, low, high)

        # 분할 지점의 왼쪽 구간을 재귀적으로 정렬
        _sort(arr, low, p)

        # 분할 지점의 오른쪽 구간을 재귀적으로 정렬
        _sort(arr, p + 1, high)

    def _partition_hoare(arr: List[int], low: int, high: int) -> int:
        # 첫 번째 원소를 피벗으로 선택
        pivot = arr[low]

        # 왼쪽 포인터: 시작 위치보다 한 칸 왼쪽
        i = low - 1

        # 오른쪽 포인터: 끝 위치보다 한 칸 오른쪽
        j = high + 1

        while True:
            # 왼쪽에서 피벗보다 크거나 같은 원소를 찾음
            i += 1
            while arr[i] < pivot:
                i += 1

            # 오른쪽에서 피벗보다 작거나 같은 원소를 찾음
            j -= 1
            while arr[j] > pivot:
                j -= 1

            # 두 포인터가 교차하면 분할 완료
            if i >= j:
                return j

            # 두 원소를 교환
            arr[i], arr[j] = arr[j], arr[i]

    # 전체 배열에 대해 정렬 수행
    _sort(result, 0, len(result) - 1)

    # 정렬된 배열을 반환
    return result


def quick_sort_three_way(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 3-way 파티션: 중복 원소가 많을 때 효과적
    def _sort(arr: List[int], low: int, high: int) -> None:
        # Base case: 구간의 크기가 1 이하이면 반환
        if low >= high:
            return

        # 랜덤 피벗 선택 (최악의 경우 방지)
        rand_idx = random.randint(low, high)
        arr[low], arr[rand_idx] = arr[rand_idx], arr[low]

        # 피벗 값 저장
        pivot = arr[low]

        # lt: 피벗보다 작은 원소의 경계
        lt = low

        # gt: 피벗보다 큰 원소의 경계
        gt = high

        # i: 현재 검사 중인 위치
        i = low + 1

        # i가 gt를 넘지 않을 때까지 반복
        while i <= gt:
            if arr[i] < pivot:
                # 피벗보다 작으면 lt 위치와 교환하고 양쪽 포인터 이동
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                # 피벗보다 크면 gt 위치와 교환하고 gt만 이동
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                # 피벗과 같으면 i만 이동
                i += 1

        # 피벗보다 작은 구간을 재귀적으로 정렬
        _sort(arr, low, lt - 1)

        # 피벗보다 큰 구간을 재귀적으로 정렬
        _sort(arr, gt + 1, high)

    # 전체 배열에 대해 정렬 수행
    _sort(result, 0, len(result) - 1)

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [10, 7, 8, 9, 1, 5]
    print(f"원본 배열: {data}")

    # Lomuto 파티션 퀵 정렬
    print(f"Lomuto:    {quick_sort_lomuto(data)}")

    # Hoare 파티션 퀵 정렬
    print(f"Hoare:     {quick_sort_hoare(data)}")

    # 3-way 파티션 퀵 정렬
    print(f"Three-Way: {quick_sort_three_way(data)}")

    # 중복 원소가 많은 배열 테스트
    dup_data = [3, 1, 2, 3, 1, 2, 3, 1, 2]
    print(f"\n중복 배열: {dup_data}")
    print(f"Three-Way: {quick_sort_three_way(dup_data)}")
