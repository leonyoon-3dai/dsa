"""
Greedy Example 8: Interval Scheduling / Merge Intervals (구간 스케줄링)

Problem 1: 겹치는 구간들을 병합하라. (LeetCode #56)
Problem 2: 겹치지 않는 최대 구간 수를 선택하라.
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # 구간이 비어있으면 빈 리스트 반환
    if not intervals:
        return []

    # 시작 시간 기준으로 오름차순 정렬
    intervals.sort(key=lambda x: x[0])

    # 병합된 결과 리스트, 첫 번째 구간으로 시작
    merged = [intervals[0]]

    # 두 번째 구간부터 순회
    for i in range(1, len(intervals)):
        # 현재 구간의 시작과 끝
        start = intervals[i][0]
        end = intervals[i][1]

        # 마지막 병합 구간의 끝
        last_end = merged[-1][1]

        # 현재 구간이 마지막 병합 구간과 겹치면
        if start <= last_end:
            # 끝을 더 큰 값으로 확장
            merged[-1][1] = max(last_end, end)
        else:
            # 겹치지 않으면 새 구간으로 추가
            merged.append([start, end])

    # 병합된 구간 리스트 반환
    return merged


def max_non_overlapping(intervals: list[list[int]]) -> list[list[int]]:
    # 겹치지 않는 최대 구간 수 선택 (끝 시간 기준 정렬)

    # 구간이 비어있으면 빈 리스트 반환
    if not intervals:
        return []

    # 종료 시간 기준 오름차순 정렬
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    # 첫 번째 구간 선택
    selected = [sorted_intervals[0]]

    # 마지막 선택 구간의 종료 시간
    last_end = sorted_intervals[0][1]

    # 두 번째 구간부터 순회
    for i in range(1, len(sorted_intervals)):
        # 현재 구간의 시작 시간이 마지막 선택의 종료 이후이면
        if sorted_intervals[i][0] >= last_end:
            # 선택 목록에 추가
            selected.append(sorted_intervals[i])
            # 종료 시간 갱신
            last_end = sorted_intervals[i][1]

    # 선택된 구간 반환
    return selected


def min_removals_for_non_overlapping(intervals: list[list[int]]) -> int:
    # 겹치지 않게 만들기 위해 제거해야 할 최소 구간 수 (LeetCode #435)

    # 구간이 비어있으면 제거할 것 없음
    if not intervals:
        return 0

    # 종료 시간 기준 오름차순 정렬
    intervals.sort(key=lambda x: x[1])

    # 유지할 구간 수 (첫 번째는 항상 유지)
    keep_count = 1

    # 마지막 유지 구간의 종료 시간
    last_end = intervals[0][1]

    # 두 번째 구간부터 순회
    for i in range(1, len(intervals)):
        # 겹치지 않으면 유지
        if intervals[i][0] >= last_end:
            keep_count += 1
            last_end = intervals[i][1]

    # 전체에서 유지 가능한 수를 빼면 제거해야 할 수
    return len(intervals) - keep_count


# === 실행 예제 ===
if __name__ == "__main__":
    # 구간 병합
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"원본 구간: {intervals1}")
    print(f"병합 결과: {merge_intervals(intervals1)}")
    print()

    # 최대 비겹침 구간
    intervals2 = [[1, 4], [2, 3], [3, 6], [5, 7], [6, 8]]
    print(f"구간: {intervals2}")
    selected = max_non_overlapping(intervals2)
    print(f"최대 비겹침 구간: {selected} ({len(selected)}개)")
    print()

    # 최소 제거
    intervals3 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(f"구간: {intervals3}")
    removals = min_removals_for_non_overlapping(intervals3)
    print(f"최소 제거 수: {removals}")
