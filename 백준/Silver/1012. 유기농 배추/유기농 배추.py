def bfs(x,y):
    queue=[(x,y)]
    farm[x][y]=0 # 방문처리(0)

    for cx, cy in queue:
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m and farm[nx][ny]:
                farm[nx][ny] = 0 #방문처리
                queue.append((nx, ny))




dx=[1,-1,0,0,] #R L U D
dy=[0,0,1,-1]

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    farm=[[0]*m for _ in range(n)] #mxn 사이즈 농장 배열 생성

    # 배추심은 곳 순회
    for _ in range(k):
        bx,by=map(int,input().split()) #배추가 심어진 좌표
        farm[bx][by]=1

    # farm 배열을 돌면서 배추가 심어진 곳(1)을 찾으면, bfs 수행하고 카운트하기
    result=0
    for i in range(n):
        for j in range(m):
            if farm[i][j]:
                bfs(i, j)  # (x,y)
                result += 1
    print(result)








