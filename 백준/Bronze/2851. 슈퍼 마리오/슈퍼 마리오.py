import sys
input=sys.stdin.readline

# 현재까지 누적합과 다음요소까지 합을 비교
# 100보다 커지는 시점에서, 이전값과 현재 누적값과 비교

total=0
scores=[int(input()) for _ in range(10)]
isDone=False

for i,s in enumerate(scores):
    total+=s  # 현재까지 누적합

    if total>=100:  # 100보다 커지는 시점
        if abs(100-total)>abs(100-(total-s)):  #97 105                         
            total-=s
            break
print(total)
















