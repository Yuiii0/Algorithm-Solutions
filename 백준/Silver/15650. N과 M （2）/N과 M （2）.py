from itertools import combinations,permutations
#1부터 n까지 중복없는 m개의 수열
n,m=input().split()

#1~n까지 리스트 생성
num_list=[i for i in range(1,int(n)+1)]


#m개의 수열 생성
combination=list(combinations(num_list,int(m)))

#출력
for c in combination:
     print(' '.join(map(str,c)))

    

