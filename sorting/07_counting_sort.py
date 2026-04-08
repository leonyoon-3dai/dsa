"""
Sorting Algorithm Example 7: Counting Sort
계수 정렬 - 원소의 출현 빈도를 세어 정렬하는 비교 기반이 아닌 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
각 원소의 등장 횟수를 세고, 누적합을 이용하여 원소의 최종 위치를 결정한다.
"""

from typing import List


def counting_sort_basic(arr: List[int]) -> List[int]:
    # 빈 배열이면 바로 반환
    if not arr:
        return []

    # 배열에서 최댓값을 찾음
    max_val = max(arr)

    # 배열에서 최솟값을 찾음
    min_val = min(arr)

    # 값의 범위 계산
    range_val = max_val - min_val + 1

    # 카운트 배열을 0으로 초기화
    count = [0] * range_val

    # 각 원소의 등장 횟수를 카운트
    for num in arr:
        # min_val을 빼서 인덱스를 0부터 시작하도록 조정
        count[num - min_val] += 1

    # 결과 배열 생성
    result = []

    # 카운트 배열을 순회하며 결과 배열을 구성
    for i in range(range_val):
        # 해당 값이 등장한 횟수만큼 결과에 추가
        result.extend([i + min_val] * count[i])

    # 정렬된 배열을 반환
    return result


def counting_sort_stable(arr: List[int]) -> List[int]:
    # 빈 배열이면 바로 반환
    if not arr:
        return []

    # 배열에서 최댓값과 최솟값을 찾음
    max_val = max(arr)
    min_val = min(arr)

    # 값의 범위 계산
    range_val = max_val - min_val + 1

    # 카운트 배열을 0으로 초기화
    count = [0] * range_val

    # 각 원소의 등장 횟수를 카운트
    for num in arr:
        count[num - min_val] += 1

    # 누적합 계산: count[i]는 i 이하의 원소가 총 몇 개인지를 나타냄
    for i in range(1, range_val):
        count[i] += count[i - 1]

    # 결과 배열을 원본과 같은 크기로 생성
    result = [0] * len(arr)

    # 뒤에서부터 순회하여 안정 정렬을 보장
    for i in range(len(arr) - 1, -1, -1):
        # 현재 원소의 카운트 인덱스
        idx = arr[i] - min_val

        # 누적합에서 1을 빼서 0-based 인덱스 계산
        count[idx] -= 1

        # 해당 위치에 원소를 배치
        result[count[idx]] = arr[i]

    # 정렬된 배열을 반환
    return result


def counting_sort_for_radix(arr: List[int], exp: int) -> List[int]:
    # 기수 정렬에서 사용하는 계수 정렬 (특정 자릿수 기준)
    n = len(arr)

    # 결과 배열 초기화
    result = [0] * n

    # 0~9까지의 숫자를 세기 위한 카운트 배열
    count = [0] * 10

    # 각 원소의 해당 자릿수 숫자를 카운트
    for num in arr:
        # exp 자릿수의 숫자를 추출 (예: exp=10이면 십의 자리)
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

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [4, 2, 2, 8, 3, 3, 1]
    print(f"원본 배열: {data}")

    # 기본 계수 정렬
    print(f"Basic:  {counting_sort_basic(data)}")

    # 안정 계수 정렬
    print(f"Stable: {counting_sort_stable(data)}")

    # 음수 포함 배열 테스트
    neg_data = [4, -1, 2, -3, 0, 3, -2]
    print(f"\n음수 포함: {neg_data}")
    print(f"Basic:  {counting_sort_basic(neg_data)}")
    print(f"Stable: {counting_sort_stable(neg_data)}")
