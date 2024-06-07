import sys
input = sys.stdin.readline
n,target=map(int,input().split())
trees=list(map(int,input().strip().split()))

left=1
right=max(trees)
result=0

while left<=right:
    mid=(left+right)//2
    count=0
    # 얻을 수 있는 나무 개수 
    for tree in trees:
        if tree>mid:
            count+=tree-mid

    # mid 조정
    if count>=target:
        result=mid
        left=mid+1
    else:
        right=mid-1
print(result)
    


