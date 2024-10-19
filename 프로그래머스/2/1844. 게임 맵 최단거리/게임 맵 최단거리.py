from collections import deque



def bfs(maps, n, m):
    queue = deque([(0, 0)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()  

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return maps[n - 1][m - 1] if maps[n - 1][m - 1] > 1 else -1


def solution(maps):
    n = len(maps)  
    m = len(maps[0]) 
    return bfs(maps, n, m)  



