"""
Sorting Algorithm Example 10: Tim Sort
팀 정렬 - 삽입 정렬과 병합 정렬을 결합한 하이브리드 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
실제 데이터에서 자주 나타나는 부분 정렬(run)을 활용하여 효율적으로 정렬한다.
Python의 내장 sort()가 사용하는 알고리즘이다.
"""

from typing import List

# Tim Sort에서 사용하는 기본 run 크기
MIN_RUN = 32


def tim_sort(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 최소 run 크기 계산
    min_run = _calc_min_run(n)

    # 배열을 run 단위로 나누어 각 run에 삽입 정렬 적용
    for start in range(0, n, min_run):
        # run의 끝 인덱스 계산 (배열 끝을 넘지 않도록)
        end = min(start + min_run - 1, n - 1)
        # 각 run에 대해 삽입 정렬 수행
        _insertion_sort_for_tim(result, start, end)

    # run들을 점점 큰 단위로 병합
    size = min_run
    while size < n:
        # 현재 크기의 run 쌍들을 병합
        for left in range(0, n, size * 2):
            # 중간 지점 계산
            mid = min(left + size - 1, n - 1)
            # 오른쪽 끝 계산
            right = min(left + 2 * size - 1, n - 1)

            # 병합할 두 부분이 모두 존재할 때만 병합 수행
            if mid < right:
                _merge_for_tim(result, left, mid, right)

        # 병합 크기를 2배로 증가
        size *= 2

    # 정렬된 배열을 반환
    return result


def _calc_min_run(n: int) -> int:
    # 최소 run 크기를 계산하는 함수
    # n을 2로 나누면서 나머지가 있으면 1을 더함
    r = 0
    while n >= MIN_RUN:
        # n이 홀수이면 r을 1로 설정
        r |= n & 1
        # n을 2로 나눔
        n >>= 1
    # n + r을 반환 (32~64 사이의 값)
    return n + r


def _insertion_sort_for_tim(arr: List[int], left: int, right: int) -> None:
    # left+1부터 right까지 삽입 정렬 수행
    for i in range(left + 1, right + 1):
        # 현재 삽입할 원소를 key에 저장
        key = arr[i]

        # 정렬된 부분의 마지막 인덱스
        j = i - 1

        # key보다 큰 원소들을 오른쪽으로 이동
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # key를 올바른 위치에 삽입
        arr[j + 1] = key


def _merge_for_tim(arr: List[int], left: int, mid: int, right: int) -> None:
    # 왼쪽 부분 배열 복사
    left_arr = arr[left:mid + 1]

    # 오른쪽 부분 배열 복사
    right_arr = arr[mid + 1:right + 1]

    # 왼쪽, 오른쪽, 결과 배열의 포인터 초기화
    i = 0       # 왼쪽 배열 포인터
    j = 0       # 오른쪽 배열 포인터
    k = left    # 결과 배열 포인터

    # 두 배열의 원소를 비교하며 병합
    while i < len(left_arr) and j < len(right_arr):
        # 왼쪽 원소가 작거나 같으면 왼쪽 원소 선택 (안정 정렬)
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # 왼쪽 배열의 남은 원소를 복사
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # 오른쪽 배열의 남은 원소를 복사
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def tim_sort_simplified(arr: List[int]) -> List[int]:
    # 단순화된 Tim Sort: 고정 run 크기 사용
    result = arr[:]
    n = len(result)

    # 고정 run 크기
    run_size = 32

    # 각 run에 삽입 정렬 적용
    for i in range(0, n, run_size):
        _insertion_sort_for_tim(result, i, min(i + run_size - 1, n - 1))

    # run들을 병합
    size = run_size
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                _merge_for_tim(result, left, mid, right)
        size *= 2

    return result


def tim_sort_pythonic(arr: List[int]) -> List[int]:
    # Python 내장 정렬 사용 (내부적으로 Tim Sort를 사용)
    result = arr[:]

    # Python의 sorted()는 Tim Sort 알고리즘을 사용
    result.sort()

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [5, 21, 7, 23, 19, 10, 12, 1, 15, 8]
    print(f"원본 배열: {data}")

    # Tim Sort 구현
    print(f"Tim Sort:      {tim_sort(data)}")

    # 단순화된 Tim Sort
    print(f"Simplified:    {tim_sort_simplified(data)}")

    # Python 내장 Tim Sort
    print(f"Pythonic:      {tim_sort_pythonic(data)}")

    # 큰 배열 테스트
    import random
    large_data = random.sample(range(1000), 50)
    print(f"\n랜덤 배열 (50개): {large_data[:10]}... (처음 10개)")
    sorted_result = tim_sort(large_data)
    print(f"정렬 결과:        {sorted_result[:10]}... (처음 10개)")

    # 부분적으로 정렬된 배열 테스트 (Tim Sort에 유리)
    partial = list(range(20)) + list(range(10, 30))
    print(f"\n부분 정렬 배열: {partial}")
    print(f"Tim Sort:      {tim_sort(partial)}")
