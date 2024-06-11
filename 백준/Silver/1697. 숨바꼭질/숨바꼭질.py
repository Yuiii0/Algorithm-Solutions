import sys
from collections import deque
input = sys.stdin.readline


# 최단경로 찾기=최단시간 찾기 (bfs)

def bfs(start,target):
    global cur
    queue=deque([start])
    visited[start]=0 #시작점은 이동거리=0

    while queue:
        cur=queue.popleft()

        if cur==target:
            return visited[cur]

        for i in range(3):
            if i<2:
                nx=cur+dx[i]
            else:
                nx=cur*dx[i]
            
            if 0 <= nx <= max(n, m) * 2 and visited[nx] == -1:
                visited[nx]=visited[cur]+1
                queue.append(nx)



n, m = map(int, input().rstrip().split())
visited = [-1] * (max(n, m) * 2 + 1) #두배까지 이동할수 있기 때문
cur = n  # 수빈 현재위치
dx = [1, -1, 2]  # 2x=cur+cur

result=bfs(cur, m)
print(result)
