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
