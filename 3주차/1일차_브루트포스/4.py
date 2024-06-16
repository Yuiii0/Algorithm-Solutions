import sys 

input = sys.stdin.readline
n = int(input().rstrip())
result=[]
for _ in range(n):
    d = int(input().rstrip())  # 수업시간
    count=0
    for t in range(1,d):
        total_time=t+(t**2)  # 지각시, 수업시간 계산
        if total_time<=d: # 같거나, 일찍 마친다면 카운트 증가 
            count+=1
        else:
            break
    result.append(count)

# 출력
for r in result:
    print(r)

# 31120	40








