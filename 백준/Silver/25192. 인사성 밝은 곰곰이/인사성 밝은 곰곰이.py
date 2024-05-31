# ENTER가 되면, 모든 참가자가 1회 인사권을 가진다. (초기화 필요)
# 값이 1이여야지 hello 카운트 가능
n=int(input())

#set..?
hello=0
users=set()
for i in range(n):
    user=input()
    if user=='ENTER':
        users=set()
    else:
        #set에 아직 존재하지 않는다=인사횟수가 남아있다.
        if user not in users:
            hello+=1
        users.add(user)

print(hello)
