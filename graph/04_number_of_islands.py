"""
Graph Algorithm Example 4: Number of Islands
섬의 개수 - BFS/DFS를 활용한 2D 그리드 탐색 문제

Problem: 2D 그리드에서 '1'은 땅, '0'은 물을 나타낸다.
상하좌우로 연결된 '1'들의 묶음(섬)의 개수를 구하라.
(LeetCode 200)
"""

from collections import deque


def num_islands_bfs(grid: list) -> int:
    # 그리드가 비어있으면 0 반환
    if not grid:
        return 0

    # 행과 열의 수
    rows = len(grid)
    cols = len(grid[0])

    # 방문 여부 기록
    visited = [[False] * cols for _ in range(rows)]

    # 섬의 개수
    count = 0

    # 상하좌우 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 모든 셀을 순회
    for r in range(rows):
        for c in range(cols):
            # 땅이고 방문하지 않은 셀을 발견하면
            if grid[r][c] == "1" and not visited[r][c]:
                # 새로운 섬 발견
                count += 1

                # BFS로 연결된 모든 땅을 방문 처리
                queue = deque([(r, c)])
                visited[r][c] = True

                while queue:
                    cr, cc = queue.popleft()

                    # 상하좌우 탐색
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc

                        # 그리드 범위 내이고, 땅이고, 미방문이면
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))

    # 섬의 개수 반환
    return count


def num_islands_dfs(grid: list) -> int:
    # 그리드가 비어있으면 0 반환
    if not grid:
        return 0

    # 입력 그리드를 변경하지 않기 위해 복사본에서 작업
    # (방문 처리를 위해 '1' -> '0'으로 덮어쓰므로, 원본을 보존하려면 복사가 필요)
    grid = [row[:] for row in grid]

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r: int, c: int):
        # 범위를 벗어나거나 물이면 종료
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        # 현재 셀을 물('0')로 변경하여 방문 처리 (복사본이므로 원본은 그대로)
        grid[r][c] = "0"

        # 상하좌우로 재귀 탐색
        dfs(r - 1, c)  # 위
        dfs(r + 1, c)  # 아래
        dfs(r, c - 1)  # 왼쪽
        dfs(r, c + 1)  # 오른쪽

    # 모든 셀을 순회
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                # 새로운 섬 발견, DFS로 연결된 땅을 모두 방문
                count += 1
                dfs(r, c)

    return count


# === 실행 예제 ===
if __name__ == "__main__":
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print("=== Number of Islands (BFS) ===")
    print(f"그리드:")
    for row in grid1:
        print(f"  {row}")
    print(f"섬의 개수: {num_islands_bfs(grid1)}")

    grid2 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(f"\n=== Number of Islands (DFS) ===")
    print(f"그리드:")
    for row in grid2:
        print(f"  {row}")
    print(f"섬의 개수: {num_islands_dfs(grid2)}")
