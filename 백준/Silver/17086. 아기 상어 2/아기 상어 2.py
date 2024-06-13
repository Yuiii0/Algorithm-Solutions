import sys
from collections import deque

input = sys.stdin.readline

# 격자의 크기를 입력 받음
m, n = map(int, input().rstrip().split())

# 8방향 이동을 위한 델타 값
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs():
    result = 0

    # 큐가 빌 때까지 반복
    while queue:
        cy, cx = queue.popleft()

        # 8방향으로 인접 리스트 순회
        for i in range(8):
            ny, nx = dy[i] + cy, dx[i] + cx

            # 격자판 내에 있고, 방문하지 않은 칸이라면
            if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 0:
                board[ny][nx] = board[cy][cx] + 1
                result = max(result, board[ny][nx])
                queue.append((ny, nx))

    return result

# 격자판 입력 받기
board = [list(map(int, input().strip().split())) for row in range(m)]

queue = deque()

# 아기상어가 위치한 곳(1) 큐에 넣기
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            queue.append((i, j))

# BFS 수행 후 결과 출력
result = bfs()
print(result - 1)  # 초기값이 1이므로 거리 계산을 위해 1을 뺌
