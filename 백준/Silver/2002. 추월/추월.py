import sys
input=sys.stdin.readline
n=int(input())

in_dict={}
out_dict={}

#입구 순서 dict 생성
for i in range(n):
    in_dict[input().rstrip()]=i

#출구 순서 dict 생성
for i in range(n):
    out_dict[input().rstrip()]=i


result=0
out_keys=list(out_dict.keys())
#출구에서 나오는 순서가 들어온순서보다 작으면👉🏻 추월
for i in range(n-1):
    name=out_keys[i] #나온 차량
    for j in range(i+1,n):
        #비교할 차량
        next_in=in_dict[out_keys[j]]
        if in_dict[name]>next_in:
            result+=1
            break
        
    
print(result)