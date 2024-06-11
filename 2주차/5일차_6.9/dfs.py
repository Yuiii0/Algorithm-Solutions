from sys import setrecursionlimit

# setrecursionlimit(10**6)

def dfs(idx):
    stack=[] # 방문해야할 노드가 담겨있다
    stack.append(idx) #stack에 삽입
    while stack:
        current=stack.pop() #stack에서 꺼내 방문
        print(f"{current}방문")
        visited=[current]=True # 방문처리

        # 인접 노드 순회하면서 연결되어있는 다른 노드
        for adj in graph[current]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj]=True
                

n=5 # 1 4 5 3 2 
graph=[[] for _ in range(n+1)] # [[],[],[],[],[],[]] 6
graph[1].append(2)
graph[1].append(4)
graph[2].append(4)
graph[4].append(1)
graph[4].append(5)
graph[5].append(3)
visited=[False]*(n+1)
dfs(1) 


#recursion
from sys import setrecursionlimit

# setrecursionlimit(10**6)

def dfs(idx):
    if visited[idx]:
        return
    visited[idx]=True #방문처리 
     # 1 2 4 5 3
    #인접 리스트 순회
    for i in graph[idx]:
        print('call할거야',i)
        dfs(i) #dfs(2) dfs(4) dfs(1) dfs(5) dfs(3) dfs(4)


                

n=5 # 1 4 5 3 2 
graph=[[] for _ in range(n+1)] # [[],[],[],[],[],[]] 6
graph[1].append(2)
graph[1].append(4)
graph[2].append(4)
graph[4].append(1)
graph[4].append(5)
graph[5].append(3)
visited=[False]*(n+1)
dfs(1) 



## ver2
# 인접 리스트로 그래프 구현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

#DFS(재귀)
def dfs(graph,start,visited=None):
    if visited is None: # 초기
        visited=set()
    visited.add(start) #방문처리
    print(start,end=' ') #방문 출력

    # 인접 순회
    for next in graph[start]:
        if next not in visited:
            dfs(graph,next,visited)

dfs(graph,'A') # A B D E F C 

        
        
