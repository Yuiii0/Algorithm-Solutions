import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start_x, start_y, end_x, end_y, length):
    queue = deque([(start_x, start_y, 0)])  
    visited = [[0] * (length + 1) for _ in range(length + 1)]
    visited[start_x][start_y] = 1

    while queue:
        cx, cy, count = queue.popleft()

        if cx == end_x and cy == end_y:  # 도착지점에 도달했을 때
            return count

        for i in range(8):
            nx, ny = dx[i] + cx, dy[i] + cy
            if 0 <= nx < length and 0 <= ny < length and visited[nx][ny] == 0:
                visited[nx][ny] = 1 
                queue.append((nx, ny, count + 1)) #현재좌표, 이동거리(시작점기준)

    return -1  # 도착지점에 도달할 수 없는 경우


n = int(input())
for _ in range(n):
    length = int(input())
    start_x, start_y = map(int, input().rstrip().split()) # 출발 지점
    end_x, end_y = map(int, input().rstrip().split())  # 도착 지점

    result = bfs(start_x, start_y, end_x, end_y, length)
    print(result)

#34072	1272