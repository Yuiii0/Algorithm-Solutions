import sys
from itertools import combinations

# 가능한 3가지 카드의 모든 조합 생성 (combinations)
# 가장 m과 가까운값 찾기

input=sys.stdin.readline
n,m=map(int,input().rstrip().split())
num_list=list(map(int,input().rstrip().split()))

result=0
for comb in combinations(num_list,3):
    # m보다 값이 작거나 같고, result에 저장해둔 현재 최대값보다 크다면, 업데이트
    if sum(comb)<=m and result<sum(comb):
        result=sum(comb) 

print(result)
    
# 31120	96



from itertools import permutations                                          
import sys                                                                  
input=sys.stdin.readline                                                    
                                                                            
n=int(input())                                                              
                                                                            
perm_list = set(permutations(list(range(1, n+1))))                          
print(len(perm_list))                                                       
                                                                            
                                                                            

                                                                            