# 새로운 유저가 들어오면, 모든 유저가 1회 인사권을 가진다.
# 값이 1이여야지 hello 카운트 가능 -> set이용
# 인사횟수가 소진된 유저=set에 존재

n=int(input())
hello=0


users=set()

for i in range(n):
    user=input()
    #새로운 유저가 입장하면, 인사횟수 초기화
    if user=='ENTER':
        users=set()
    else:
        #set에 아직 존재하지 않는다=인사횟수가 남아있다.
        if user not in users:
            hello+=1            
        users.add(user)

print(hello)
