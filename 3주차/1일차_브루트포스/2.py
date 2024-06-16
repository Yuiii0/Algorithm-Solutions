import sys
from itertools import permutations

# 가능한 3가지 모든 조합 생성 (permutations)
# 중복되는 값은 제외 (set)
# 1~12시가 아닌 H 제외

input=sys.stdin.readline
times=map(int,input().rstrip().split(':')) #시 분 초

result=set()
for i,comb in enumerate(permutations(times,3)):
    print(i,comb)
    if i<=1: #1번째=시
        if comb[0]<=12:
            result.add(comb)
    elif i==2 or i==4: #2번째 시
         if comb[0]<=12:
            result.add(comb)
    else: #3번째 시
         if comb[0]<=12:
            result.add(comb)





import sys
from itertools import permutations

# 가능한 3가지 모든 조합 생성 순서 (permutations)
# 1~12시가 아닌 H 제외

input=sys.stdin.readline
times=map(int,input().rstrip().split(':')) #시 분 초

result=0
for i,comb in enumerate(permutations(times,3)):
    # 유효성 검사
    if comb[0]>59 or comb[1]>59 or comb[2]>59 :
        break
    print(comb)
    if 0<comb[0]<=12:  # 1~12시만 카운트
        result+=1


print(result)






# 31120	40
    

print(result)
print(len(result))

