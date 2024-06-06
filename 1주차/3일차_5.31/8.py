# 1. 듣지 못한 사람, 보지 못한 사람 리스트 따로 만들어서 교집합으로 구하기
# 2. 공통의 dict만들어서 value가 2인사람=듣보잡

n,m=input().split()


#명단 dict 생성
users={}

for i in range(int(n)+int(m)):
    name=input()
    users[name]=users.get(name,0)+1

# dict_items([('ohhenrie', 2), ('charlie', 1), ('baesangwook', 2), ('obama', 1), ('clinton', 1)])

#value가 2인 듣보잡 찾기
result=list(filter(lambda x:x[1]==2, users.items())).sort()
result.sort()

#출력
print(len(result))
for r in result:
    print(r[0]) #듣보잡 출력

