"""
Sorting Algorithm Example 8: Radix Sort
기수 정렬 - 자릿수별로 정렬을 반복하는 비교 기반이 아닌 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
가장 낮은 자릿수부터 가장 높은 자릿수까지 안정 정렬을 반복 적용한다.
"""

from typing import List


def radix_sort_lsd(arr: List[int]) -> List[int]:
    # 빈 배열이면 바로 반환
    if not arr:
        return []

    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열에서 최댓값을 찾음 (자릿수 결정용)
    max_val = max(result)

    # LSD (Least Significant Digit): 가장 낮은 자릿수부터 정렬
    # exp는 현재 처리 중인 자릿수 (1, 10, 100, ...)
    exp = 1

    # 최댓값의 모든 자릿수를 처리할 때까지 반복
    while max_val // exp > 0:
        # 현재 자릿수 기준으로 계수 정렬 수행
        result = _counting_sort_by_digit(result, exp)
        # 다음 자릿수로 이동
        exp *= 10

    # 정렬된 배열을 반환
    return result


def _counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
    # 배열 길이 저장
    n = len(arr)

    # 결과 배열 초기화
    result = [0] * n

    # 0~9까지의 숫자를 세기 위한 카운트 배열
    count = [0] * 10

    # 각 원소의 해당 자릿수 숫자를 카운트
    for num in arr:
        # exp 자릿수의 숫자를 추출
        digit = (num // exp) % 10
        count[digit] += 1

    # 누적합 계산
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 뒤에서부터 순회하여 안정 정렬 보장
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        result[count[digit]] = arr[i]

    # 정렬된 배열 반환
    return result


def radix_sort_msd(arr: List[int]) -> List[int]:
    # 빈 배열이면 바로 반환
    if not arr:
        return []

    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 최댓값의 자릿수를 계산
    max_val = max(result)
    max_digits = len(str(max_val))

    # MSD (Most Significant Digit): 가장 높은 자릿수부터 정렬
    def _msd_sort(arr: List[int], exp: int) -> List[int]:
        # Base case: 배열 크기가 1 이하이거나 자릿수를 모두 처리했으면 반환
        if len(arr) <= 1 or exp <= 0:
            return arr

        # 0~9까지의 버킷을 생성
        buckets = [[] for _ in range(10)]

        # 각 원소를 해당 자릿수의 숫자에 따라 버킷에 분배
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        # 각 버킷을 재귀적으로 정렬한 후 결과를 합침
        result = []
        for bucket in buckets:
            # 버킷 내의 원소들을 다음 자릿수 기준으로 재귀 정렬
            result.extend(_msd_sort(bucket, exp // 10))

        return result

    # 가장 높은 자릿수부터 시작
    exp = 10 ** (max_digits - 1)

    # MSD 정렬 수행
    return _msd_sort(result, exp)


def radix_sort_negative(arr: List[int]) -> List[int]:
    # 빈 배열이면 바로 반환
    if not arr:
        return []

    # 음수와 양수를 분리
    negatives = [-x for x in arr if x < 0]  # 음수를 양수로 변환
    positives = [x for x in arr if x >= 0]   # 양수만 추출

    # 양수 부분을 기수 정렬
    sorted_pos = radix_sort_lsd(positives) if positives else []

    # 음수 부분을 양수로 변환 후 기수 정렬
    sorted_neg = radix_sort_lsd(negatives) if negatives else []

    # 음수 부분을 다시 음수로 변환하고 역순으로 배치
    sorted_neg = [-x for x in reversed(sorted_neg)]

    # 음수 + 양수를 합쳐서 반환
    return sorted_neg + sorted_pos


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"원본 배열: {data}")

    # LSD 기수 정렬
    print(f"LSD: {radix_sort_lsd(data)}")

    # MSD 기수 정렬
    print(f"MSD: {radix_sort_msd(data)}")

    # 음수 포함 배열 테스트
    neg_data = [170, -45, 75, -90, 802, -24, 2, 66]
    print(f"\n음수 포함: {neg_data}")
    print(f"Negative: {radix_sort_negative(neg_data)}")
