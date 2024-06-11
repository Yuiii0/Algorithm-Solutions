import sys
from collections import deque

input = sys.stdin.readline

def bfs(idx):
    queue=deque([(start)])
    visited[idx]=0

    while queue:
        cur=queue.popleft()

        for neighbor in graph[cur]:
            if visited[neighbor]==-1:
                queue.append(neighbor)
                visited[neighbor]=visited[cur]+1
                #print('neighbor',neighbor,visited[neighbor])
                if visited[neighbor]==target:
                    answer.append(neighbor)
                    # print('find',neighbor)
                    # print(result)
    return answer





n, m, target, start = map(int, input().rstrip().split())

graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

visited=[-1]*(n+1) # start 기준 거리
answer=[]
result=bfs(start)



# 출력
if not answer:
    print(-1)
else:
    print('\n'.join(map(str, sorted(result))))




# 98800	2152