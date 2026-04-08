"""
Sorting Algorithm Example 4: Merge Sort
병합 정렬 - 배열을 반으로 나누고, 정렬한 후 병합하는 분할 정복 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
배열을 재귀적으로 반씩 분할한 뒤, 정렬된 부분 배열들을 병합한다.
"""

from typing import List


def merge_sort_recursive(arr: List[int]) -> List[int]:
    # Base case: 배열의 크기가 1 이하이면 이미 정렬됨
    if len(arr) <= 1:
        return arr[:]

    # 배열을 반으로 나누기 위한 중간 인덱스 계산
    mid = len(arr) // 2

    # 왼쪽 절반을 재귀적으로 정렬
    left = merge_sort_recursive(arr[:mid])

    # 오른쪽 절반을 재귀적으로 정렬
    right = merge_sort_recursive(arr[mid:])

    # 정렬된 두 부분 배열을 병합하여 반환
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    # 병합 결과를 저장할 리스트
    result = []

    # 두 배열의 현재 비교 위치를 가리키는 포인터
    i = 0  # 왼쪽 배열 포인터
    j = 0  # 오른쪽 배열 포인터

    # 두 배열 모두 원소가 남아있는 동안 반복
    while i < len(left) and j < len(right):
        # 왼쪽 원소가 작거나 같으면 왼쪽 원소를 결과에 추가 (안정 정렬)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        # 오른쪽 원소가 작으면 오른쪽 원소를 결과에 추가
        else:
            result.append(right[j])
            j += 1

    # 왼쪽 배열에 남은 원소를 모두 추가
    result.extend(left[i:])

    # 오른쪽 배열에 남은 원소를 모두 추가
    result.extend(right[j:])

    # 병합된 결과 반환
    return result


def merge_sort_bottom_up(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 부분 배열의 크기를 1부터 시작하여 2배씩 증가
    size = 1
    while size < n:
        # 현재 크기의 부분 배열들을 병합
        for start in range(0, n, size * 2):
            # 왼쪽 부분 배열의 범위: [start, mid)
            mid = min(start + size, n)
            # 오른쪽 부분 배열의 범위: [mid, end)
            end = min(start + size * 2, n)

            # 두 부분 배열을 병합
            merged = _merge(result[start:mid], result[mid:end])

            # 병합된 결과를 원래 위치에 복사
            result[start:start + len(merged)] = merged

        # 부분 배열의 크기를 2배로 증가
        size *= 2

    # 정렬된 배열을 반환
    return result


def merge_sort_inplace(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 내부 재귀 함수 정의
    def _sort(arr: List[int], left: int, right: int) -> None:
        # Base case: 구간의 크기가 1 이하이면 반환
        if left >= right:
            return

        # 중간 인덱스 계산
        mid = (left + right) // 2

        # 왼쪽 절반 정렬
        _sort(arr, left, mid)

        # 오른쪽 절반 정렬
        _sort(arr, mid + 1, right)

        # 임시 배열에 병합 결과 저장
        temp = []
        i = left      # 왼쪽 부분 배열 포인터
        j = mid + 1   # 오른쪽 부분 배열 포인터

        # 두 부분 배열의 원소를 비교하며 병합
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        # 남은 원소들을 추가
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1

        # 병합된 결과를 원래 배열에 복사
        for k in range(len(temp)):
            arr[left + k] = temp[k]

    # 전체 배열에 대해 정렬 수행
    _sort(result, 0, len(result) - 1)

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"원본 배열: {data}")

    # 재귀 병합 정렬
    print(f"Recursive:  {merge_sort_recursive(data)}")

    # 상향식 병합 정렬
    print(f"Bottom-Up:  {merge_sort_bottom_up(data)}")

    # 제자리 병합 정렬
    print(f"In-Place:   {merge_sort_inplace(data)}")

    # 큰 배열 테스트
    import random
    large_data = random.sample(range(100), 20)
    print(f"\n랜덤 배열: {large_data}")
    print(f"정렬 결과: {merge_sort_recursive(large_data)}")
