# 확장자별 카운터
# 확장자 사전순 정렬

n=int(input())

#.을 기준으로 name,type 
files={}
for _ in range(n):
    name,type=input().split('.')
    files[type]=files.get(type,0)+1

#sorted
result=sorted(files.items(),key=lambda x:x[0])

for type,count in result:
    print(type,count)


##########################





#문자열 이용

n = int(input())

# 확장자를 문자열로 저장
files = ""

for _ in range(n):
    name, type = input().split('.')
    files += type + " "

# 확장자를 사전 순으로 정렬
sorted_types = sorted(set(files.split()))

# 각 확장자의 개수를 세어 출력
for type in sorted_types:
    count = files.count(type)
    print(type, count)
