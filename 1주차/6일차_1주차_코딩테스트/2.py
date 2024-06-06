import sys
input=sys.stdin.readline

board=[]
# 오목판 배열 생성
for _ in range(19):
    l=list(map(int,input().split()))
    board.append(l)

#[left_diagonal,right_diagonal,down,right]
black=[]
white=[] 

for i in range(19): #row
    for j in range(19): #col
        if 0<=i and i<19 and 0<=j and j<19: #인덱스 범위안에서
            cur=board[i][j]
            if cur==0:
                continue
                
            left_diagonal=board[i+1][j-1]
            right_diagonal=board[i+1][j+1]
            down=board[i+1][j]
            right=board[i][j+1]

            #print('현재',cur,'위치',i,j)
            if cur==right_diagonal:
                for x in range(2,5): # 2 3 4 
                    next=board[i+x][j+x]
                    if cur!=next: #안맞으면
                        break
                          
                    #print('next틀렸나',next,x)
                    if x==4: #5번까지 맞다면
                        if next!=board[i+5][j+5]:
                            print(cur)
                            print(i+1,j+1)
            if cur==left_diagonal:
                  for x in range(2,5): # 2 3 4 
                      next=board[i+x][j-x]
                      if cur!=next: 
                          break
                      if x==4: 
                          if next!=board[i-5][j-5]:
                              print(cur)
                              print(i-1,j+1)
            if cur==down:
                  for x in range(2,5): # 2 3 4 
                      next=board[i+x][j]
                      if cur!=next: 
                          break
                      if x==4: 
                          if next!=board[i+5][j]:
                              print(cur)
                              print(i+1,j+1)
            if cur==right:
                  for x in range(2,5): # 2 3 4 
                      next=board[i][j+x]
                      if cur!=next: 
                          break
                      if x==4: 
                          if next!=board[i][j+5]:
                              print(cur)
                              print(i+1,j+1)

                  
                    
                    
                    



            




        # 오른쪽, 아래 check



print(board)

