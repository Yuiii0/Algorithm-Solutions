import sys
from heapq import *
input=sys.stdin.readline

INF=float('inf')

def dijkstra(start):
    dist=[INF]*len(graph)
    dist[start]=0 #시작점 거리는 0
    q=[(0,start)] #(cost,노드번호)
    while q:
        cost,idx=heappop(q)
        if dist[idx]<cost: # 무시(이미 방문했거나, 갱신할 필요가 없음)
            continue

        # 인접 노드 순회
        for adj,d in graph[idx]: #노드번호,cost
            if cost+d<dist[adj]: # 시작지점 기준으로 현재 방문중인 (꺼낸) 노드까지 비용+인접노드 비용이 기록중인 dist보다 작으면
                # 갱신
                dist[adj]=cost+d
                # 더 짧은 경로 창로를 찾은 노드들은 다시 우선순위 큐에 넣는다!
                heappush(q,(dist[adj],adj)) #(새로운 최단cost,노드번호)
    return dist





v,e=map(int,input().rstrip().split())
start=int(input())

graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append((b,c)) # (노드번호, cost) 2,5중 2번 노드 먼저 순회

# 다익스트라
distance=dijkstra(start)

for i in range(1,v+1):
    print(distance[i] if distance[i]!=INF else 'INF')


