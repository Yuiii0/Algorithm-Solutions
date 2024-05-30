#test개수 추출
n=int(input())

#test번 순회하면서 반복할 횟수(r)와 문자열(s)추출하고,
#문자열(s)순회하면서 r번만큼 반복

for i in range(n):
    r,s=input().split()
    for c in s:
        print(c*int(r),end='')
    print('')    
        
