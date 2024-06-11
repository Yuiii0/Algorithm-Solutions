#queue
def bfs(idx):
    from collectioins import deque
    queue=deque()
    queue.append(idx) #방문해야할 노드 큐에 넣고
    visited[idx]=True

    while queue:
        idx=queue.popleft()
        print(f"{idx} 방문")
        # 인접 방문
        for i in graph[idx]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n=5 # 1 4 5 3 2(dfs)  # 1 2 4 5 3(bfs)
graph=[[] for _ in range(n+1)] # [[],[],[],[],[],[]] 6
graph[1].append(2)
graph[1].append(4)
graph[2].append(4)
graph[4].append(1)
graph[4].append(5)
graph[5].append(3)
visited=[False]*(n+1)
dfs(1) 


from collections import deque
# 인접 리스트로 그래프 구현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph,start):
    visited=set()
    queue=deque([start])
    
    while queue:
        vertex=queue.popleft()
        
        if vertex not in visited:
            visited.add(vertex)
            print(vertex,end=' ')
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)