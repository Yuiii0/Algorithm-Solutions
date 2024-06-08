# 31120	44

import sys
input = sys.stdin.readline

# time이 오름차순일때, 최소값

n=int(input())
times=list(map(int,input().strip().split()))

# (idx,time)형태 리스트 생성
watings=[(i+1,time) for i,time in enumerate(times)]


# time순 sort
result=0
temp=0
watings.sort(key=lambda x:x[1])
for waiting in watings:
    time=waiting[1]
    temp+=time
    result+=temp
print(result)




        
        


    