import sys
from collections import deque

input = sys.stdin.readline

# 촌수거리= 최단거리 찾기 bfs
# visited 배열에 start지점부터 이동거리 저장
# target 도달시, visited[cur] 

def bfs(start,end):

    queue=deque([start])
    visited[start]=0 # 시작지점: 거리 0

    while queue:
        cur=queue.popleft()

        # 목표 지점 도달하면 거리 반환
        if cur==end:
            return 
           

       # 인접 노드 방문

        for neighbor in graph[cur]:
            if visited[neighbor]==-1: # 방문하지 않은 노드
                queue.append(neighbor)
                visited[neighbor]=visited[cur]+1


    return -1

n = int(input())
start, end = map(int, input().rstrip().split())  # target


graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1) # start 기준 거리

m = int(input())

for _ in range(m):
    p, c = map(int, input().rstrip().split())
    graph[p].append(c)
    graph[c].append(p)

result=bfs(start,end)
print(result)

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start,end):

    queue=deque([start])
    visited[start]=0 # 시작지점: 거리 0

    while queue:
        cur=queue.popleft()

        # 목표 지점 도달하면 거리 반환
        if cur==end:
            return visited[cur]
           

       # 인접 노드 방문

        for neighbor in graph[cur]:
            if visited[neighbor]==-1: # 방문하지 않은 노드
                queue.append(neighbor)
                visited[neighbor]=visited[cur]+1


    return -1

n = int(input())
start, end = map(int, input().rstrip().split())  # target


graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1) # start 기준 거리

m = int(input())

for _ in range(m):
    p, c = map(int, input().rstrip().split())
    graph[p].append(c)
    graph[c].append(p)

result=bfs(start,end)
print(result)


#34044	60


#7 3
# 7 방문
# 2 방문
# 1 방문
# 8 방문
# 9 방문
# 3 방문
# 도착 3

















