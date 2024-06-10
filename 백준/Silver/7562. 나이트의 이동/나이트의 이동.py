import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start_x, start_y, end_x, end_y, length):
    queue = deque([(start_x, start_y, 0)])  # 큐에 이동 횟수도 함께 저장
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
                queue.append((nx, ny, count + 1))

    return -1  # 도착지점에 도달할 수 없는 경우


n = int(input())
for _ in range(n):
    length = int(input())
    start_x, start_y = map(int, input().rstrip().split())
    end_x, end_y = map(int, input().rstrip().split())

    result = bfs(start_x, start_y, end_x, end_y, length)
    print(result)
