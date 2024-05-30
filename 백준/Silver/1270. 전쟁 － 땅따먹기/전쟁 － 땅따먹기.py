# 카운트해서 최빈 군번 구하기
# 분기
# 1. 최빈 군번이 절반 초과 O -> 군번출력
# 2. 최빈 군번이 절반 초과 X -> SYJKGW 출력

from collections import Counter

n=int(input())


#최빈 군번 찾기
for i in range(n):
    l=input().split()
    counter=Counter(l).most_common(1)

    winner=counter[0]
    # print(winner[1])
    # print(len(l)/2)


    #절반 초과 확인
    if winner[1]>=len(l)/2:
        print(winner[0])
    else:
        print('SYJKGW')
    
    
