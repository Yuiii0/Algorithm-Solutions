import sys
input=sys.stdin.readline

n,k=map(int,input().split())
lines=[int(input()) for _ in range(n)]

answer=1
left=1
right=2**31-1

#binary Search
while left<=right:
    mid=(left+right)//2
    count=0 # 생성되는 막대 개수
    for line in lines:
        count+=line//mid # mid로 인해 생성되는 막대 개수 카운트
        
    if count>=k: #오른쪽 보기
        answer=mid
        left=mid+1
    
    else:
        right=mid-1
print(answer)
        



