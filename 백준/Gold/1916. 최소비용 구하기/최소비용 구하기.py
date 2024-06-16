from sys import stdin
from heapq import heappop,heappush
input = stdin.readline

INF=float('inf')

def dijkstra(start):
    dist = [INF] * len(graph)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, idx = heappop(q)
        if dist[idx] < cost:
            continue

        for adj, d in graph[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(q, (dist[adj], adj))
    return dist


n=int(input().strip())
m=int(input().strip())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().strip().split())
    graph[a].append((b,c))

start,end=map(int,input().strip().split())

distance=dijkstra(start)
print(distance[end])






