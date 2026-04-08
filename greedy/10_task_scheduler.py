"""
Greedy Example 10: Task Scheduler (작업 스케줄러)

Problem: 작업 배열 tasks와 쿨다운 시간 n이 주어진다.
         같은 작업 사이에 최소 n 단위 시간의 간격이 필요하다.
         모든 작업을 완료하는 데 필요한 최소 시간을 구하라.
LeetCode #621
"""

from collections import Counter


def task_scheduler_greedy(tasks: list[str], n: int) -> int:
    # 각 작업의 빈도수를 계산
    freq = Counter(tasks)

    # 가장 높은 빈도수
    max_freq = max(freq.values())

    # 가장 높은 빈도수를 가진 작업의 개수
    max_count = sum(1 for f in freq.values() if f == max_freq)

    # 공식: (max_freq - 1) * (n + 1) + max_count
    # (max_freq - 1): 마지막 그룹 제외한 그룹 수
    # (n + 1): 각 그룹의 크기 (작업 1개 + 쿨다운 n)
    # max_count: 마지막 그룹의 작업 수
    result = (max_freq - 1) * (n + 1) + max_count

    # 결과가 전체 작업 수보다 작으면 전체 작업 수가 답
    # (쿨다운 없이 빈틈없이 채울 수 있는 경우)
    return max(result, len(tasks))


def task_scheduler_simulation(tasks: list[str], n: int) -> int:
    # 시뮬레이션 방식: 실제로 스케줄을 구성

    # 빈도수 계산
    freq = Counter(tasks)

    # (빈도수, 작업) 형태의 리스트를 빈도 내림차순으로 정렬
    task_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # 현재 시간
    time = 0
    # 스케줄 결과 (디버깅/확인용)
    schedule = []

    # 남은 작업이 있는 동안 반복
    while task_list:
        # 현재 라운드에서 처리할 작업을 담을 임시 리스트
        temp = []
        # 이번 라운드에서 처리한 작업 수
        count = 0

        # n+1개의 슬롯을 채움 (1작업 + n쿨다운)
        for i in range(n + 1):
            # 처리할 작업이 남아있으면
            if i < len(task_list):
                # 작업 이름과 남은 횟수
                task_name, task_freq = task_list[i]
                # 스케줄에 추가
                schedule.append(task_name)
                # 횟수가 1보다 크면 감소시켜서 다음 라운드에 포함
                if task_freq > 1:
                    temp.append((task_name, task_freq - 1))
                # 처리 카운트 증가
                count += 1
            elif temp or i < n + 1:
                # 작업이 없어도 아직 쿨다운 채워야 할 수 있음
                if temp:
                    # idle 슬롯 추가
                    schedule.append("idle")
                    count += 1

        # 시간 경과
        time += count if not temp else max(count, n + 1)

        # 남은 작업으로 리스트 갱신 (빈도 내림차순 정렬)
        task_list = sorted(temp, key=lambda x: x[1], reverse=True)

        # 남은 작업이 없으면 종료
        if not task_list:
            break

    # 총 소요 시간 반환
    return time


def task_scheduler_formula_explained(tasks: list[str], n: int) -> tuple[int, str]:
    # 공식의 동작 원리를 설명과 함께 반환

    # 빈도수 계산
    freq = Counter(tasks)
    # 최대 빈도
    max_freq = max(freq.values())
    # 최대 빈도를 가진 작업 수
    max_count = sum(1 for f in freq.values() if f == max_freq)
    # 전체 작업 수
    total_tasks = len(tasks)

    # 프레임 수 = (max_freq - 1) 개의 완전한 블록 + 마지막 블록
    frames = (max_freq - 1) * (n + 1) + max_count

    # 설명 문자열 생성
    explanation = (
        f"최대 빈도: {max_freq}, 최대 빈도 작업 수: {max_count}\n"
        f"프레임 계산: ({max_freq}-1) * ({n}+1) + {max_count} = {frames}\n"
        f"전체 작업 수: {total_tasks}\n"
        f"최종 결과: max({frames}, {total_tasks}) = {max(frames, total_tasks)}"
    )

    # (결과, 설명) 반환
    return max(frames, total_tasks), explanation


# === 실행 예제 ===
if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    print(f"작업: {tasks}")
    print(f"쿨다운: {n}")
    print()

    result1 = task_scheduler_greedy(tasks, n)
    print(f"그리디 결과: {result1}")

    result2, explanation = task_scheduler_formula_explained(tasks, n)
    print(f"\n공식 설명:")
    print(explanation)

    print()
    tasks2 = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n2 = 2
    print(f"작업: {tasks2}")
    print(f"쿨다운: {n2}")
    result3 = task_scheduler_greedy(tasks2, n2)
    print(f"그리디 결과: {result3}")
