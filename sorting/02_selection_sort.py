"""
Sorting Algorithm Example 2: Selection Sort
선택 정렬 - 매 단계에서 최솟값을 찾아 앞으로 이동시키는 알고리즘

Problem: 주어진 배열을 오름차순으로 정렬하라.
정렬되지 않은 부분에서 최솟값을 선택하여 정렬된 부분의 끝에 배치한다.
"""

from typing import List


def selection_sort_basic(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 0부터 n-2까지 반복 (마지막 원소는 자동으로 정렬됨)
    for i in range(n - 1):
        # 현재 위치를 최솟값의 인덱스로 가정
        min_idx = i

        # i+1부터 끝까지 탐색하여 최솟값의 인덱스를 찾음
        for j in range(i + 1, n):
            # 현재 최솟값보다 더 작은 값을 발견하면 인덱스 갱신
            if result[j] < result[min_idx]:
                min_idx = j

        # 최솟값을 현재 위치로 교환 (제자리로 이동)
        result[i], result[min_idx] = result[min_idx], result[i]

    # 정렬된 배열을 반환
    return result


def selection_sort_stable(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 안정 정렬 버전: 교환 대신 삽입 방식 사용
    for i in range(n - 1):
        # 현재 위치를 최솟값의 인덱스로 가정
        min_idx = i

        # i+1부터 끝까지 탐색하여 최솟값의 인덱스를 찾음
        for j in range(i + 1, n):
            # 현재 최솟값보다 더 작은 값을 발견하면 인덱스 갱신
            if result[j] < result[min_idx]:
                min_idx = j

        # 최솟값을 임시 저장
        min_val = result[min_idx]

        # 최솟값 위치부터 현재 위치까지 원소를 한 칸씩 뒤로 이동
        while min_idx > i:
            result[min_idx] = result[min_idx - 1]
            min_idx -= 1

        # 최솟값을 현재 위치에 삽입 (안정성 유지)
        result[i] = min_val

    # 정렬된 배열을 반환
    return result


def selection_sort_bidirectional(arr: List[int]) -> List[int]:
    # 원본 배열을 보호하기 위해 복사본 생성
    result = arr[:]

    # 배열의 길이를 저장
    n = len(result)

    # 왼쪽(최솟값)과 오른쪽(최댓값) 경계를 설정
    left = 0
    right = n - 1

    # 양쪽 경계가 만날 때까지 반복
    while left < right:
        # 현재 범위에서 최솟값과 최댓값의 인덱스를 초기화
        min_idx = left
        max_idx = left

        # 현재 범위를 탐색하여 최솟값과 최댓값을 동시에 찾음
        for i in range(left, right + 1):
            # 최솟값 인덱스 갱신
            if result[i] < result[min_idx]:
                min_idx = i
            # 최댓값 인덱스 갱신
            if result[i] > result[max_idx]:
                max_idx = i

        # 최솟값을 왼쪽 경계로 이동
        result[left], result[min_idx] = result[min_idx], result[left]

        # 최댓값 인덱스가 왼쪽 경계에 있었다면 스왑으로 인해 위치가 변경됨
        if max_idx == left:
            max_idx = min_idx

        # 최댓값을 오른쪽 경계로 이동
        result[right], result[max_idx] = result[max_idx], result[right]

        # 경계를 좁힘
        left += 1
        right -= 1

    # 정렬된 배열을 반환
    return result


# === 실행 예제 ===
if __name__ == "__main__":
    # 테스트용 배열
    data = [64, 25, 12, 22, 11]
    print(f"원본 배열: {data}")

    # 기본 선택 정렬
    print(f"Basic:         {selection_sort_basic(data)}")

    # 안정 선택 정렬
    print(f"Stable:        {selection_sort_stable(data)}")

    # 양방향 선택 정렬
    print(f"Bidirectional: {selection_sort_bidirectional(data)}")

    # 역순 배열 테스트
    reverse_data = [5, 4, 3, 2, 1]
    print(f"\n역순 배열: {reverse_data}")
    print(f"Basic:         {selection_sort_basic(reverse_data)}")
