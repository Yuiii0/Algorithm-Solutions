#enter: 추가
#leave: 삭제

n=int(input())

active={}
for i in range(n):
    name,status=input().split()
    if status=='enter':
        active[name]=True
    else:
        del active[name]

#출력
sorted_list=sorted(active.keys(),reverse=True)
for key in sorted_list:
    print(key)
