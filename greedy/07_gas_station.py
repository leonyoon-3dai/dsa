"""
Greedy Example 7: Gas Station (주유소 문제)

Problem: 원형으로 배치된 주유소가 있고, 각 주유소의 가스량과 다음 주유소까지의
         비용이 주어진다. 시계 방향으로 한 바퀴 돌 수 있는 출발 주유소의
         인덱스를 구하라. 불가능하면 -1을 반환.
LeetCode #134
"""


def gas_station_greedy(gas: list[int], cost: list[int]) -> int:
    # 전체 가스의 합과 비용의 합을 비교
    total_gas = sum(gas)
    total_cost = sum(cost)

    # 전체 가스가 전체 비용보다 적으면 해결 불가능
    if total_gas < total_cost:
        return -1

    # 출발 후보 인덱스
    start = 0
    # 현재 탱크에 남은 가스
    tank = 0

    # 모든 주유소를 순회
    for i in range(len(gas)):
        # 현재 주유소에서 가스를 넣고 다음까지의 비용을 뺌
        tank += gas[i] - cost[i]

        # 탱크가 음수가 되면 현재 출발점에서는 불가능
        if tank < 0:
            # 다음 주유소를 새로운 출발 후보로 설정
            start = i + 1
            # 탱크 초기화
            tank = 0

    # 출발 인덱스 반환 (전체 합이 0 이상이면 반드시 답이 존재)
    return start


def gas_station_brute_force(gas: list[int], cost: list[int]) -> int:
    # 브루트포스: 모든 출발점을 시도
    n = len(gas)

    # 각 주유소를 출발점으로 시도
    for start in range(n):
        # 현재 탱크
        tank = 0
        # 성공 여부 플래그
        success = True

        # 한 바퀴 순회
        for j in range(n):
            # 현재 방문 중인 주유소 인덱스 (원형)
            idx = (start + j) % n
            # 가스를 넣고 비용을 뺌
            tank += gas[idx] - cost[idx]

            # 탱크가 음수가 되면 이 출발점은 실패
            if tank < 0:
                success = False
                break

        # 한 바퀴를 성공적으로 돌았으면 이 출발점이 답
        if success:
            return start

    # 어떤 출발점도 불가능
    return -1


def gas_station_with_trace(gas: list[int], cost: list[int]) -> tuple[int, list[int]]:
    # 경로 추적이 포함된 그리디 방식
    total_gas = sum(gas)
    total_cost = sum(cost)

    # 해결 불가능한 경우
    if total_gas < total_cost:
        return -1, []

    # 출발 후보와 탱크 초기화
    start = 0
    tank = 0

    # 출발점 탐색
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0

    # 출발점에서의 경로를 시뮬레이션
    n = len(gas)
    tank = 0
    # 각 주유소 도착 후 탱크 잔량 기록
    tank_trace = []

    for j in range(n):
        idx = (start + j) % n
        # 가스 충전
        tank += gas[idx]
        # 탱크 잔량 기록 (이동 전)
        tank_trace.append(tank)
        # 이동 비용 차감
        tank -= cost[idx]

    # (출발 인덱스, 탱크 잔량 기록) 반환
    return start, tank_trace


# === 실행 예제 ===
if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    print(f"가스: {gas}")
    print(f"비용: {cost}")
    print()

    result1 = gas_station_greedy(gas, cost)
    print(f"그리디 출발 인덱스: {result1}")

    result2 = gas_station_brute_force(gas, cost)
    print(f"브루트포스 출발 인덱스: {result2}")

    start, trace = gas_station_with_trace(gas, cost)
    print(f"\n출발 인덱스: {start}")
    if start != -1:
        print("경로 탱크 잔량:", trace)
