import sys
input=sys.stdin.readline

n=int(input())
peaks=list(map(int,input().rstrip().split()))

best_man=peaks[0]
count_list=[]
count=0
for i in range(1,len(peaks)):
    if best_man>peaks[i]: # 처치 가능
        count+=1
    else:
        count_list.append(count)
        count=0 # 초기화
        best_man=peaks[i]
count_list.append(count)
print(max(count_list))














