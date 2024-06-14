from sys import stdin
from heapq import heappop,heappush
input = stdin.readline
t=int(input())

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


for _ in range(t):
    n,d,c=map(int,input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a,b,s = map(int, input().split())
        graph[b].append((a,s)) # 역방향으로 넣어줌 (의존과 전염은 역관계)


    #다익스트라
    distance=dijkstra(c) # 해킹당한 컴퓨터 기준 최단거리 리스트
    result=list(filter(lambda x:x!=INF,distance)) # 감염된 컴퓨터=인접
    print(len(result),max(result))







