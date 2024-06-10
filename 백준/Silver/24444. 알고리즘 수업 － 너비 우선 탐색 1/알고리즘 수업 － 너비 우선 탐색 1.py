import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def bfs(idx):
    global cnt
    queue=deque([idx])
    visited[idx]=cnt

    while queue:
        vertex=queue.popleft()
        #인접 노드 확인
        for i in graph[vertex]:
            if visited[i]==0:
                queue.append(i)
                cnt+=1 #순서 업데이트
                visited[i]=cnt



n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt=1 # 방문 순서

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 순서로 인접노드를 방문하기 위해 정렬
for g in graph:
    g.sort()

bfs(r)

# 출력
for i in range(1, n + 1):
    print(visited[i])




