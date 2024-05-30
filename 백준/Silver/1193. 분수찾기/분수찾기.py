n = int(input())
line = 1

# 1. 몇 번째 라인인지 찾기
while n>0 and n>line:
    n-=line
    if n<=0:
        break
    line+=1

# 2. 라인 홀짝여부에 따른 분기 (a/b)
if line%2==0: 
    a=n
    b=line-n+1
else:
    a=line-n+1
    b=n

print(f'{a}/{b}')
