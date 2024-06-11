import sys
input = sys.stdin.readline

def dfs(idx):
    stack.append(idx)
    visited[idx] = True
    
    while stack:
        cur = stack.pop()
        for i in graph[cur]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                answer.add(i)

n, m = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().strip().split())
    graph[end].append(start)

target = int(input().strip())

stack = []
answer = set()

dfs(target)  # 뒤에서부터 역추적

print(len(answer))
