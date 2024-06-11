import sys
input=sys.stdin.readline

n,m=map(int,input().strip().split())
z = m * 100 // n # 현재 승률 


if z >= 99:
    print(-1)
else:
    
    
    start=1
    end=n
    
    result=0
    while start<=end:
        mid=(start+end)//2
        new_z = (m + mid) * 100 // (n + mid)
        if z+1<=new_z: #오른쪽 탐색
            result=mid
            end=mid-1
        else:
            start=mid+1
    print(result)    