"""
Greedy Example 9: Assign Cookies (쿠키 배분)

Problem: 아이들의 욕심 값 g[]와 쿠키 크기 s[]가 주어진다.
         쿠키 크기가 아이의 욕심 값 이상이면 만족한다.
         최대 몇 명의 아이를 만족시킬 수 있는가?
LeetCode #455
"""


def assign_cookies_greedy(g: list[int], s: list[int]) -> int:
    # 아이들의 욕심 값을 오름차순 정렬
    g_sorted = sorted(g)
    # 쿠키 크기를 오름차순 정렬
    s_sorted = sorted(s)

    # 아이 포인터 (욕심이 작은 아이부터)
    child = 0
    # 쿠키 포인터 (작은 쿠키부터)
    cookie = 0

    # 두 포인터 모두 범위 내일 때 반복
    while child < len(g_sorted) and cookie < len(s_sorted):
        # 현재 쿠키가 현재 아이의 욕심을 만족시키면
        if s_sorted[cookie] >= g_sorted[child]:
            # 아이를 만족시켰으므로 다음 아이로 이동
            child += 1
        # 쿠키는 항상 다음으로 이동 (사용했거나 너무 작거나)
        cookie += 1

    # 만족한 아이의 수 반환 (child 포인터가 곧 만족한 수)
    return child


def assign_cookies_reverse(g: list[int], s: list[int]) -> int:
    # 역방향: 큰 쿠키부터 욕심 많은 아이에게 배분

    # 내림차순 정렬
    g_sorted = sorted(g, reverse=True)
    s_sorted = sorted(s, reverse=True)

    # 만족한 아이 수
    count = 0
    # 쿠키 포인터
    cookie = 0

    # 욕심이 큰 아이부터 순회
    for child_greed in g_sorted:
        # 쿠키가 남아있고, 현재 쿠키가 욕심을 만족시키면
        if cookie < len(s_sorted) and s_sorted[cookie] >= child_greed:
            # 만족 카운트 증가
            count += 1
            # 다음 쿠키로 이동
            cookie += 1

    # 만족한 아이의 수 반환
    return count


def assign_cookies_brute_force(g: list[int], s: list[int]) -> int:
    # 브루트포스: 모든 할당 조합 중 최대를 찾음 (작은 입력용)

    # 각 쿠키의 사용 여부 추적
    used = [False] * len(s)
    # 만족한 아이 수
    count = 0

    # 욕심이 작은 아이부터 정렬하여 순회
    for greed in sorted(g):
        # 최적의 쿠키를 찾기 위한 변수
        best_cookie = -1
        best_size = float("inf")

        # 모든 쿠키를 확인
        for j in range(len(s)):
            # 아직 사용하지 않은 쿠키이고 욕심을 만족시키면
            if not used[j] and s[j] >= greed:
                # 가장 작은 적합 쿠키를 선택 (낭비 최소화)
                if s[j] < best_size:
                    best_size = s[j]
                    best_cookie = j

        # 적합한 쿠키를 찾았으면
        if best_cookie != -1:
            # 해당 쿠키를 사용 표시
            used[best_cookie] = True
            # 만족 카운트 증가
            count += 1

    # 결과 반환
    return count


# === 실행 예제 ===
if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]

    print(f"아이 욕심 값: {g}")
    print(f"쿠키 크기: {s}")
    print(f"정방향 그리디: {assign_cookies_greedy(g, s)}명 만족")
    print(f"역방향 그리디: {assign_cookies_reverse(g, s)}명 만족")
    print(f"브루트포스: {assign_cookies_brute_force(g, s)}명 만족")
    print()

    g2 = [1, 2]
    s2 = [1, 2, 3]
    print(f"아이 욕심 값: {g2}")
    print(f"쿠키 크기: {s2}")
    print(f"정방향 그리디: {assign_cookies_greedy(g2, s2)}명 만족")
    print(f"역방향 그리디: {assign_cookies_reverse(g2, s2)}명 만족")
    print(f"브루트포스: {assign_cookies_brute_force(g2, s2)}명 만족")
