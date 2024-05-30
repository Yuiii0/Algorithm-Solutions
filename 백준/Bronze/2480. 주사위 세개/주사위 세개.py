#3가지 조건문에 따른 분기#
#-------------------#

#각 주사위 숫자 추출
a, b, c = map(int, input().split())

#3개 일치하는 경우
if a==b==c:
    print(10000+a*1000)
#2개 일치하는 경우
elif a==b or a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
#1개 일치하는 경우
else:
    print(max(a,b,c)*100)









