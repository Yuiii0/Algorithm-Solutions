#최고점을 찾아 순회하면서 계산식 적용

n=int(input())
score_list=list(map(int,input().split()))

max_score=max(score_list)


result=0
for score in score_list:
    result+=score/max_score*100

print(result/n)