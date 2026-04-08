"""
Greedy Example 5: Minimum Platforms (최소 플랫폼 문제)

Problem: 기차의 도착 시간과 출발 시간이 주어질 때,
         모든 기차가 정차할 수 있도록 필요한 최소 플랫폼 수를 구하라.
"""


def minimum_platforms_sorting(
    arrivals: list[int], departures: list[int]
) -> int:
    # 도착 시간 오름차순 정렬
    arrivals_sorted = sorted(arrivals)
    # 출발 시간 오름차순 정렬
    departures_sorted = sorted(departures)

    # 기차 수
    n = len(arrivals)

    # 현재 필요한 플랫폼 수
    platforms_needed = 0
    # 최대 플랫폼 수 (결과)
    max_platforms = 0

    # 도착 배열의 포인터
    i = 0
    # 출발 배열의 포인터
    j = 0

    # 두 포인터를 이용하여 이벤트를 시간순으로 처리
    while i < n and j < n:
        # 도착 이벤트가 출발 이벤트보다 먼저이거나 같으면
        if arrivals_sorted[i] <= departures_sorted[j]:
            # 플랫폼 하나 추가 필요
            platforms_needed += 1
            # 최대값 갱신
            max_platforms = max(max_platforms, platforms_needed)
            # 다음 도착 이벤트로 이동
            i += 1
        else:
            # 출발 이벤트 처리: 플랫폼 하나 해제
            platforms_needed -= 1
            # 다음 출발 이벤트로 이동
            j += 1

    # 최소 플랫폼 수 반환
    return max_platforms


def minimum_platforms_event(
    arrivals: list[int], departures: list[int]
) -> int:
    # 이벤트 기반 접근: (시간, 타입) 형태로 이벤트 생성
    events = []

    # 도착 이벤트는 +1 (플랫폼 필요)
    for t in arrivals:
        events.append((t, 1))

    # 출발 이벤트는 -1 (플랫폼 해제)
    for t in departures:
        # 출발은 도착보다 나중에 처리하기 위해 +0.5
        events.append((t + 0.5, -1))

    # 시간 기준으로 정렬
    events.sort()

    # 현재 플랫폼 수
    current = 0
    # 최대 플랫폼 수
    max_platforms = 0

    # 모든 이벤트를 순회
    for time, event_type in events:
        # 도착이면 +1, 출발이면 -1
        current += event_type
        # 최대값 갱신
        max_platforms = max(max_platforms, current)

    # 결과 반환
    return max_platforms


def minimum_platforms_brute_force(
    arrivals: list[int], departures: list[int]
) -> int:
    # 브루트포스: 모든 시점에서 겹치는 기차 수를 확인
    n = len(arrivals)

    # 최대 플랫폼 수
    max_platforms = 0

    # 각 기차의 도착 시간을 기준으로 확인
    for i in range(n):
        # 현재 시점에서 정차 중인 기차 수
        count = 0

        # 모든 기차에 대해 겹치는지 확인
        for j in range(n):
            # j번째 기차가 i번째 기차 도착 시점에 정차 중인지
            if arrivals[j] <= arrivals[i] and departures[j] >= arrivals[i]:
                count += 1

        # 최대값 갱신
        max_platforms = max(max_platforms, count)

    # 결과 반환
    return max_platforms


# === 실행 예제 ===
if __name__ == "__main__":
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]

    print(f"도착 시간: {arrivals}")
    print(f"출발 시간: {departures}")
    print()

    result1 = minimum_platforms_sorting(arrivals, departures)
    print(f"정렬 방식 최소 플랫폼: {result1}")

    result2 = minimum_platforms_event(arrivals, departures)
    print(f"이벤트 방식 최소 플랫폼: {result2}")

    result3 = minimum_platforms_brute_force(arrivals, departures)
    print(f"브루트포스 최소 플랫폼: {result3}")
