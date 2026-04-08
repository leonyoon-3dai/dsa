# DSA Study (자료구조 & 알고리즘 스터디)

Python으로 작성된 알고리즘 학습 저장소. 각 카테고리별 10개의 예제와 한국어 라인별 주석, 상세 문서를 포함합니다.

## Categories

| # | Folder | Topic | Description |
|---|--------|-------|-------------|
| 1 | [`dp/`](dp/) | Dynamic Programming (동적 프로그래밍) | 피보나치, 배낭 문제, LCS, LIS, 편집 거리 등 |
| 2 | [`graph/`](graph/) | Graph (그래프) | BFS, DFS, 다익스트라, 벨만-포드, MST 등 |
| 3 | [`sorting/`](sorting/) | Sorting (정렬) | 버블, 선택, 삽입, 병합, 퀵, 힙, 기수 정렬 등 |
| 4 | [`tree/`](tree/) | Tree (트리) | 순회, BST, LCA, 직렬화, 균형 트리 등 |
| 5 | [`greedy/`](greedy/) | Greedy (그리디) | 활동 선택, 배낭, 허프만, 구간 스케줄링 등 |

## Folder Structure

각 카테고리는 동일한 구조를 따릅니다:

```
category/
├── README.md                # 카테고리 개요 및 예제 목록
├── 01_example.py            # Python 코드 (한국어 라인별 주석)
├── 02_example.py
├── ...
├── 10_example.py
└── docs/
    ├── 01_example.md        # 상세 한국어 설명 문서
    ├── 02_example.md
    ├── ...
    └── 10_example.md
```

## Features

- **한국어 주석**: 모든 Python 파일에 라인별 한국어 주석 포함
- **상세 문서**: `docs/` 폴더에 접근법별 라인별 설명, 실행 예제, 복잡도 비교 포함
- **다중 접근법**: 각 문제마다 2~3가지 풀이 방법 제시
- **실행 가능**: 모든 파일에 `if __name__ == "__main__"` 블록 포함

## Usage

```bash
# 특정 예제 실행
python3 dp/01_fibonacci.py
python3 graph/01_bfs.py
python3 sorting/04_merge_sort.py
python3 tree/05_validate_bst.py
python3 greedy/06_jump_game.py
```

## Topics

### Dynamic Programming (동적 프로그래밍)
| # | Topic |
|---|-------|
| 1 | Fibonacci (피보나치) |
| 2 | Climbing Stairs (계단 오르기) |
| 3 | Coin Change (동전 거스름돈) |
| 4 | LCS (최장 공통 부분 수열) |
| 5 | 0/1 Knapsack (배낭 문제) |
| 6 | LIS (최장 증가 부분 수열) |
| 7 | Edit Distance (편집 거리) |
| 8 | House Robber (도둑 문제) |
| 9 | Maximum Subarray (최대 부분 배열) |
| 10 | Unique Paths (고유 경로) |

### Graph (그래프)
| # | Topic |
|---|-------|
| 1 | BFS (너비 우선 탐색) |
| 2 | DFS (깊이 우선 탐색) |
| 3 | Dijkstra (다익스트라 최단 경로) |
| 4 | Number of Islands (섬의 개수) |
| 5 | Topological Sort (위상 정렬) |
| 6 | Cycle Detection (순환 탐지) |
| 7 | Bellman-Ford (벨만-포드) |
| 8 | Floyd-Warshall (플로이드-워셜) |
| 9 | Kruskal's MST (최소 신장 트리) |
| 10 | Bipartite Check (이분 그래프 판별) |

### Sorting (정렬)
| # | Topic |
|---|-------|
| 1 | Bubble Sort (버블 정렬) |
| 2 | Selection Sort (선택 정렬) |
| 3 | Insertion Sort (삽입 정렬) |
| 4 | Merge Sort (병합 정렬) |
| 5 | Quick Sort (퀵 정렬) |
| 6 | Heap Sort (힙 정렬) |
| 7 | Counting Sort (계수 정렬) |
| 8 | Radix Sort (기수 정렬) |
| 9 | Shell Sort (셸 정렬) |
| 10 | Tim Sort (팀 정렬) |

### Tree (트리)
| # | Topic |
|---|-------|
| 1 | Inorder Traversal (중위 순회) |
| 2 | Preorder & Postorder (전위/후위 순회) |
| 3 | Level Order Traversal (레벨 순회) |
| 4 | Maximum Depth (최대 깊이) |
| 5 | Validate BST (이진 탐색 트리 검증) |
| 6 | LCA (최소 공통 조상) |
| 7 | BST Operations (이진 탐색 트리 연산) |
| 8 | Diameter of Binary Tree (이진 트리 지름) |
| 9 | Serialize & Deserialize (직렬화/역직렬화) |
| 10 | Balanced Binary Tree (균형 이진 트리) |

### Greedy (그리디)
| # | Topic |
|---|-------|
| 1 | Activity Selection (활동 선택) |
| 2 | Fractional Knapsack (분할 가능 배낭) |
| 3 | Huffman Coding (허프만 코딩) |
| 4 | Job Sequencing (작업 스케줄링) |
| 5 | Minimum Platforms (최소 플랫폼) |
| 6 | Jump Game (점프 게임) |
| 7 | Gas Station (주유소 문제) |
| 8 | Interval Scheduling (구간 스케줄링) |
| 9 | Assign Cookies (쿠키 배분) |
| 10 | Task Scheduler (작업 스케줄러) |
