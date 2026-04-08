"""
Greedy Example 2: Fractional Knapsack (분할 가능 배낭 문제)

Problem: 각 물건의 무게와 가치가 주어질 때,
         배낭의 용량 W를 초과하지 않으면서 최대 가치를 얻어라.
         물건을 쪼개서 일부만 담을 수 있다.
"""


def fractional_knapsack_greedy(
    weights: list[float], values: list[float], capacity: float
) -> float:
    # 물건의 개수
    n = len(weights)

    # (가치/무게 비율, 무게, 가치) 형태로 리스트 생성
    items = []
    for i in range(n):
        # 단위 무게당 가치 계산
        ratio = values[i] / weights[i]
        # 튜플로 저장
        items.append((ratio, weights[i], values[i]))

    # 단위 무게당 가치 기준으로 내림차순 정렬 (가치 효율이 높은 것부터)
    items.sort(key=lambda x: x[0], reverse=True)

    # 현재까지 담은 총 가치
    total_value = 0.0

    # 남은 배낭 용량
    remaining = capacity

    # 가치 효율이 높은 물건부터 순회
    for ratio, weight, value in items:
        # 배낭에 여유가 없으면 종료
        if remaining <= 0:
            break

        # 물건 전체를 담을 수 있는 경우
        if weight <= remaining:
            # 물건 전체를 담음
            total_value += value
            # 남은 용량에서 물건 무게만큼 차감
            remaining -= weight
        else:
            # 물건의 일부만 담는 경우 (분할)
            # 남은 용량만큼의 비율로 가치를 계산
            total_value += ratio * remaining
            # 배낭이 가득 참
            remaining = 0

    # 최대 가치 반환
    return total_value


def fractional_knapsack_with_detail(
    weights: list[float], values: list[float], capacity: float
) -> tuple[float, list[tuple[int, float]]]:
    # 물건의 개수
    n = len(weights)

    # (비율, 원본 인덱스) 형태로 리스트 생성
    indexed_items = []
    for i in range(n):
        # 단위 무게당 가치와 원본 인덱스를 함께 저장
        ratio = values[i] / weights[i]
        indexed_items.append((ratio, i))

    # 비율 기준 내림차순 정렬
    indexed_items.sort(key=lambda x: x[0], reverse=True)

    # 총 가치 초기화
    total_value = 0.0
    # 남은 용량
    remaining = capacity
    # 각 물건을 얼마나 담았는지 기록 (인덱스, 비율)
    taken = []

    # 정렬된 순서대로 물건을 담음
    for ratio, idx in indexed_items:
        # 용량이 없으면 종료
        if remaining <= 0:
            break

        # 담을 수 있는 무게 계산 (전체 또는 남은 용량)
        take_weight = min(weights[idx], remaining)
        # 해당 무게에 대한 가치 계산
        take_value = ratio * take_weight
        # 총 가치에 추가
        total_value += take_value
        # 남은 용량 차감
        remaining -= take_weight
        # 담은 비율 기록 (0.0 ~ 1.0)
        fraction = take_weight / weights[idx]
        taken.append((idx, fraction))

    # (총 가치, 담은 내역) 반환
    return total_value, taken


# === 실행 예제 ===
if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    print(f"무게: {weights}")
    print(f"가치: {values}")
    print(f"배낭 용량: {capacity}")
    print()

    # 기본 그리디
    result = fractional_knapsack_greedy(weights, values, capacity)
    print(f"최대 가치 (그리디): {result}")
    print()

    # 상세 결과 포함
    total, taken = fractional_knapsack_with_detail(weights, values, capacity)
    print(f"최대 가치 (상세): {total}")
    for idx, frac in taken:
        print(f"  물건 {idx}: 무게={weights[idx]}, 가치={values[idx]}, "
              f"담은 비율={frac:.2f} ({frac*100:.0f}%)")
