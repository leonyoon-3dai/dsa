"""
Sorting Algorithm Example 9: Shell Sort
셸 정렬 - 간격(gap)을 줄여가며 삽입 정렬을 수행하는 개선된 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
큰 간격으로 시작하여 점차 간격을 줄이면서 삽입 정렬을 반복 적용한다.
"""

from typing import List


def shell_sort_basic(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 초기 간격: 배열 길이의 절반
    gap = n // 2

    # 간격이 0보다 큰 동안 반복
    while gap > 0:
        # gap 간격으로 떨어진 원소들에 대해 삽입 정렬 수행
        for i in range(gap, n):
            # 현재 삽입할 원소를 temp에 저장
            temp = result[i]

            # gap 간격으로 앞의 원소들과 비교
            j = i
            while j >= gap and result[j - gap] > temp:
                # 앞의 원소를 gap 간격만큼 뒤로 이동
                result[j] = result[j - gap]
                # 비교 위치를 gap만큼 앞으로 이동
                j -= gap

            # temp를 올바른 위치에 삽입
            result[j] = temp

        # 간격을 절반으로 줄임
        gap //= 2

    # 정렬된 배열을 반환
    return result


def shell_sort_knuth(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # Knuth 간격 수열: 1, 4, 13, 40, 121, ... (h = 3h + 1)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1  # 간격을 증가시킴

    # 간격이 0보다 큰 동안 반복
    while gap >= 1:
        # gap 간격으로 삽입 정렬 수행
        for i in range(gap, n):
            # 현재 삽입할 원소를 temp에 저장
            temp = result[i]

            # gap 간격으로 앞의 원소들과 비교
            j = i
            while j >= gap and result[j - gap] > temp:
                # 앞의 원소를 gap 간격만큼 뒤로 이동
                result[j] = result[j - gap]
                j -= gap

            # temp를 올바른 위치에 삽입
            result[j] = temp

        # Knuth 간격 축소: h = (h - 1) / 3
        gap //= 3

    # 정렬된 배열을 반환
    return result


def shell_sort_hibbard(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # Hibbard 간격 수열: 1, 3, 7, 15, 31, ... (2^k - 1)
    # 먼저 간격 수열을 생성
    gaps = []
    k = 1
    while (2 ** k - 1) < n:
        gaps.append(2 ** k - 1)
        k += 1

    # 가장 큰 간격부터 역순으로 처리
    for gap in reversed(gaps):
        # gap 간격으로 삽입 정렬 수행
        for i in range(gap, n):
            # 현재 삽입할 원소를 temp에 저장
            temp = result[i]

            # gap 간격으로 앞의 원소들과 비교
            j = i
            while j >= gap and result[j - gap] > temp:
                # 앞의 원소를 gap 간격만큼 뒤로 이동
                result[j] = result[j - gap]
                j -= gap

            # temp를 올바른 위치에 삽입
            result[j] = temp

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [23, 12, 1, 8, 34, 54, 2, 3]
    print(f"원본 배열: {data}")

    # 기본 셸 정렬 (Shell의 원래 간격: n/2)
    print(f"Basic (Shell):  {shell_sort_basic(data)}")

    # Knuth 간격 수열 셸 정렬
    print(f"Knuth:          {shell_sort_knuth(data)}")

    # Hibbard 간격 수열 셸 정렬
    print(f"Hibbard:        {shell_sort_hibbard(data)}")

    # 큰 배열 테스트
    import random
    large_data = random.sample(range(100), 20)
    print(f"\n랜덤 배열: {large_data}")
    print(f"Knuth 정렬: {shell_sort_knuth(large_data)}")
