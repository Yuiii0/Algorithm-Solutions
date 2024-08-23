from collections import deque

# 상하좌우 이동을 위한 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, start_x, start_y, end_x, end_y):
    queue = deque([(start_x, start_y)])
    rows, cols = len(graph), len(graph[0])
    visited = [[-1] * cols for _ in range(rows)]  # 방문 여부 및 최단 거리 저장

    visited[start_x][start_y] = 0  # 시작점은 0으로 설정

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx, cy
            # 로봇이 이동할 수 있을 때까지 반복
            while 0 <= nx + dx[i] < rows and 0 <= ny + dy[i] < cols and graph[nx + dx[i]][ny + dy[i]] != 0:
                nx += dx[i]
                ny += dy[i]

            # 해당 위치를 처음 방문할 때만 큐에 추가
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx, ny))

            # 도착
            if nx == end_x and ny == end_y:
                return visited[nx][ny]  # 도착 지점까지의 최단 거리 반환

    return -1  # 도착할 수 없는 경우

def solution(board):
    graph = []
    start_x, start_y, end_x, end_y = -1, -1, -1, -1

    for i, b in enumerate(board):
        row = []
        if 'R' in b:
            start_y = b.index('R')
            start_x = i
        if 'G' in b:
            end_y = b.index('G')
            end_x = i
        for char in b:
            if char == 'D':
                row.append(0)
            else:
                row.append(1)
        graph.append(row)

    if start_x == -1 or end_x == -1:
        return -1

    return bfs(graph, start_x, start_y, end_x, end_y)


