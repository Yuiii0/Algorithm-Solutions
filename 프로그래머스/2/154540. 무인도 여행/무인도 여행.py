from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    queue = deque([(x, y)])
    count = 0
    
    while queue:
        x, y = queue.popleft()
        
        if graph[x][y] == 0:
            continue
        
        count += graph[x][y]
        graph[x][y] = 0  # 방문 처리
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] > 0:
                queue.append((nx, ny))
    
    return count

def solution(maps):
    graph = []
    for m in maps:
        m = m.replace('X', '0')
        graph.append(list(map(int, list(m))))
    
    answer = []
    
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] > 0:  # 아직 방문하지 않은 경우
                count = bfs(x, y, graph)
                answer.append(count)
    
    if answer:
        return sorted(answer)
    else:
        return [-1]


