"""
Greedy Example 4: Job Sequencing with Deadlines (작업 스케줄링)

Problem: 각 작업에 마감일(deadline)과 이익(profit)이 주어질 때,
         한 번에 하나의 작업만 수행할 수 있고 각 작업은 1단위 시간이 걸린다.
         마감일 전에 완료하면 이익을 얻는다. 최대 이익을 구하라.
"""


def job_sequencing_greedy(
    jobs: list[tuple[str, int, int]]
) -> tuple[int, list[str]]:
    # jobs: (작업ID, 마감일, 이익) 형태의 리스트

    # 이익 기준 내림차순 정렬 (이익이 큰 작업부터 배치)
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # 최대 마감일 찾기 (시간 슬롯의 범위 결정)
    max_deadline = max(job[1] for job in jobs)

    # 시간 슬롯 배열: None이면 비어있음
    slots = [None] * (max_deadline + 1)

    # 총 이익
    total_profit = 0
    # 선택된 작업 목록
    selected = []

    # 이익이 큰 작업부터 순회
    for job_id, deadline, profit in sorted_jobs:
        # 마감일부터 1까지 역순으로 빈 슬롯 탐색
        for t in range(deadline, 0, -1):
            # 해당 시간 슬롯이 비어있으면 배치
            if slots[t] is None:
                # 슬롯에 작업 배치
                slots[t] = job_id
                # 이익 추가
                total_profit += profit
                # 선택 목록에 추가
                selected.append(job_id)
                # 배치했으면 다음 작업으로
                break

    # (총 이익, 선택된 작업 목록) 반환
    return total_profit, selected


def job_sequencing_with_union_find(
    jobs: list[tuple[str, int, int]]
) -> tuple[int, list[str]]:
    # Union-Find를 사용한 최적화 버전

    # 이익 기준 내림차순 정렬
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # 최대 마감일
    max_deadline = max(job[1] for job in jobs)

    # parent[i] = i번 슬롯의 부모 (Union-Find)
    parent = list(range(max_deadline + 1))

    def find(x: int) -> int:
        # 경로 압축을 사용한 Find 연산
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # 총 이익과 선택된 작업 목록
    total_profit = 0
    selected = []

    # 이익이 큰 작업부터 순회
    for job_id, deadline, profit in sorted_jobs:
        # 배치 가능한 가장 늦은 슬롯 찾기
        available = find(deadline)

        # 사용 가능한 슬롯이 있으면 (0보다 큰 슬롯)
        if available > 0:
            # 해당 슬롯 사용 표시 (이전 슬롯과 Union)
            parent[available] = available - 1
            # 이익 추가
            total_profit += profit
            # 선택 목록에 추가
            selected.append(job_id)

    # (총 이익, 선택된 작업 목록) 반환
    return total_profit, selected


# === 실행 예제 ===
if __name__ == "__main__":
    # (작업ID, 마감일, 이익)
    jobs = [("J1", 2, 100), ("J2", 1, 19), ("J3", 2, 27),
            ("J4", 1, 25), ("J5", 3, 15)]

    print("작업 목록:")
    for job_id, deadline, profit in jobs:
        print(f"  {job_id}: 마감일={deadline}, 이익={profit}")
    print()

    # 기본 그리디
    profit1, selected1 = job_sequencing_greedy(jobs)
    print(f"그리디 결과: 선택={selected1}, 총 이익={profit1}")

    # Union-Find 최적화
    profit2, selected2 = job_sequencing_with_union_find(jobs)
    print(f"Union-Find 결과: 선택={selected2}, 총 이익={profit2}")
