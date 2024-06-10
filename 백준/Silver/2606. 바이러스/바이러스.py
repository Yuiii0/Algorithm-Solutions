def bfs(idx):
    stack=[idx]
    #stack.append(idx)
    visited[idx]=True

    while stack:
        cur=stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj]=True
                stack.append(adj)




# 그래프 초기 설정
n=int(input())
graph=[[] for _ in range(n+1)] #0번째 인덱스는 빈배열로

for _ in range(int(input())):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색
visited=[False]*(n+1)
bfs(1)

# 1번노드 제외하고 방문한 노드 개수 카운트하기
result=0
for i in range(2,n+1):
    if visited[i]:
        result+=1
print(result)