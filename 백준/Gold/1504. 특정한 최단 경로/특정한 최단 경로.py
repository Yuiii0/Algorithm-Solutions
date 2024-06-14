import sys
from heapq import heappop,heappush
input=sys.stdin.readline
INF=float('inf')

def dijkstra(start):
    dist=[INF]*len(graph)
    dist[start]=0

    q=[(0,start)]
    while q:
        cost,idx=heappop(q)
        if dist[idx]<cost:
            continue

        for adj,d in graph[idx]:
            if cost+d<dist[adj]:
                dist[adj]=cost+d
                heappush(q,(dist[adj],adj))
    return dist



n,e=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append((b,c)) #(노드번호,cost)
    graph[b].append((a,c))

v1,v2=map(int,input().rstrip().split())


distance=dijkstra(1) # 1 출발 기준 dist
v1_dist=dijkstra(v1) # v1 출발 기준 dist
v1_v2_dist=v1_dist[v2] # v1,v2사이의 거리
v2_dist=dijkstra(v2) # v2 출발 기준 dist


path1=distance[v1]+v1_v2_dist+v2_dist[n] # 1-v1-v2-N
path2=distance[v2]+v1_v2_dist+v1_dist[n] # 1-v2-v1-N

# 경로가 없는 경우 확인
if any(x >= INF for x in [distance[v1], v1_dist[v2], v2_dist[n], distance[v2], v2_dist[v1], v1_dist[n]]):
    print(-1)
else:
    print(min(path1, path2))




