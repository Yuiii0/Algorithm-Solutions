import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

cnt=1
def dfs(idx):
    global cnt
    if visited[idx]:
        return
    visited[idx] = cnt  # 방문한 순서

    # 인접리스트 순회하면서 dfs 재귀호출
    for i in graph[idx]:
        if visited[i]==0:  # 방문안한 노드
            cnt+=1
            dfs(i)


n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)


for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 순서로 인접노드를 방문하기 위해 정렬
for g in graph:
    g.sort()

dfs(r)


# 출력
for i in range(1, n + 1):
    print(visited[i])



# 67996	744
