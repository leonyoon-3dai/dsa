"""
Greedy Example 1: Activity Selection (활동 선택 문제)

Problem: 시작 시간과 종료 시간이 주어진 활동들 중에서,
         서로 겹치지 않는 최대 개수의 활동을 선택하라.
"""


def activity_selection_greedy(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # 활동을 종료 시간 기준으로 오름차순 정렬
    sorted_acts = sorted(activities, key=lambda x: x[1])

    # 첫 번째 활동은 무조건 선택 (종료가 가장 빠른 활동)
    selected = [sorted_acts[0]]

    # 마지막으로 선택한 활동의 종료 시간을 기록
    last_end = sorted_acts[0][1]

    # 두 번째 활동부터 순회
    for i in range(1, len(sorted_acts)):
        # 현재 활동의 시작 시간
        start = sorted_acts[i][0]
        # 현재 활동의 종료 시간
        end = sorted_acts[i][1]

        # 현재 활동의 시작이 마지막 선택 활동의 종료 이후라면 선택
        if start >= last_end:
            # 겹치지 않으므로 선택 목록에 추가
            selected.append((start, end))
            # 마지막 종료 시간 갱신
            last_end = end

    # 선택된 활동 목록 반환
    return selected


def activity_selection_dp(activities: list[tuple[int, int]]) -> int:
    # 종료 시간 기준으로 정렬
    sorted_acts = sorted(activities, key=lambda x: x[1])

    # 활동 개수
    n = len(sorted_acts)

    # dp[i] = 0~i번째 활동까지 고려했을 때 선택할 수 있는 최대 활동 수
    dp = [0] * n

    # 첫 번째 활동은 무조건 1개 선택 가능
    dp[0] = 1

    # 두 번째 활동부터 순회
    for i in range(1, n):
        # 현재 활동을 선택하지 않는 경우: 이전까지의 최대값
        exclude = dp[i - 1]

        # 현재 활동을 선택하는 경우: 겹치지 않는 마지막 활동 찾기
        include = 1
        # 현재 활동의 시작 시간
        start_i = sorted_acts[i][0]

        # i-1부터 0까지 역순으로 탐색
        for j in range(i - 1, -1, -1):
            # j번째 활동의 종료 시간이 현재 시작 이전이면
            if sorted_acts[j][1] <= start_i:
                # j까지의 최대값 + 현재 활동 1개
                include = dp[j] + 1
                # 찾았으면 탐색 종료
                break

        # 선택/비선택 중 최대값을 dp에 저장
        dp[i] = max(exclude, include)

    # 전체 최대 활동 수 반환
    return dp[n - 1]


def activity_selection_recursive(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # 종료 시간 기준으로 정렬
    sorted_acts = sorted(activities, key=lambda x: x[1])

    def helper(index: int, last_end: int) -> list[tuple[int, int]]:
        # 모든 활동을 확인했으면 빈 리스트 반환
        if index == len(sorted_acts):
            return []

        # 현재 활동의 시작 시간과 종료 시간
        start, end = sorted_acts[index]

        # 현재 활동이 겹치지 않으면 선택하고 다음으로 진행
        if start >= last_end:
            # 현재 활동을 선택하고, 이후 활동들에서 재귀적으로 선택
            return [(start, end)] + helper(index + 1, end)
        else:
            # 겹치면 현재 활동을 건너뛰고 다음 활동으로 진행
            return helper(index + 1, last_end)

    # 초기 호출: 인덱스 0, 이전 종료 시간 0
    return helper(0, 0)


# === 실행 예제 ===
if __name__ == "__main__":
    # (시작 시간, 종료 시간) 형태의 활동 목록
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
                  (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

    print("활동 목록:", activities)
    print()

    # 그리디 방식
    result1 = activity_selection_greedy(activities)
    print(f"그리디 선택 결과: {result1}")
    print(f"선택된 활동 수: {len(result1)}")
    print()

    # DP 방식 (최대 개수만 반환)
    result2 = activity_selection_dp(activities)
    print(f"DP 최대 활동 수: {result2}")
    print()

    # 재귀 방식
    result3 = activity_selection_recursive(activities)
    print(f"재귀 선택 결과: {result3}")
    print(f"선택된 활동 수: {len(result3)}")
