#31120	44

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

#croatia의 패턴을 빈문자열로 대체하면 또 새로운 패턴이 생길 수 있기 때문에 * 
for c in croatia :
    s = s.replace(c, '*') 
print(len(s)) 


######################################
#틀렸는데, 처음 접근법
import sys
alphabets=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s=sys.stdin.readline()

result=0
# 해당 패턴이 존재해서, 문자열을 쪼갤수 있다면 업데이트를 해줘야함 문자열로
# 해당 패턴이 여러개 존재할수있다

# ❗️문자열로 합치면서 새로운 크로아티아 조합이 생길수 있기때문에 빈문자로 join
for alpha in alphabets:
    if len(s.split(alpha))>1:
        c=s.count(alpha)
        result+=c
        s='*'.join(s.split(alpha))
        print(s)


#크로아티아 아닌 알파벳 카운트
result+=len(s.replace("*", ""))
print(result)