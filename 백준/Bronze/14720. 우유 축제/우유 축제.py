import sys
input=sys.stdin.readline

# milks, stores 두개의 포인터 사용
# 두 값이 일치하면, 둘 다 이동
# 일치하지 않다면, store 포인터만 이동

n=int(input())
stores=list(map(int,input().rstrip().split()))
milks=[0,1,2]*500
count=0

i=0
for s in range(len(stores)):
    # print('포인터 위치',s,i,stores[s],milks[i])
    if stores[s]==milks[i]:
        i+=1 #milk 포인터도 이동
        count+=1
print(count)



    # for j in range(milks):
    #     print('포인터 위치', i, j, stores[i], milks[j])
    #     if stores[i] == milks[j]:
    #         i += 1  # 두 포인터 이동
    #     else:  # 일치하지 않다면, stores만 이동
    #         i += 1


























