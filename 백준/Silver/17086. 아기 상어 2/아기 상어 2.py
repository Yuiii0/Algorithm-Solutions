import sys
from collections import deque

input = sys.stdin.readline


m, n = map(int, input().rstrip().split())


dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs():
    result = 0


    while queue:
        cy, cx = queue.popleft()


        for i in range(8):
            ny, nx = dy[i] + cy, dx[i] + cx

            # 상어가 없는 0에 대해 이동 거리 계산
            if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 0:
                board[ny][nx] = board[cy][cx] + 1
                result = max(result, board[ny][nx])
                queue.append((ny, nx))

    return result


board = [list(map(int, input().strip().split())) for row in range(m)]

queue = deque()

# 아기상어가 위치한 곳(1) 큐에 넣기
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            queue.append((i, j))


result = bfs()
print(result - 1)  
