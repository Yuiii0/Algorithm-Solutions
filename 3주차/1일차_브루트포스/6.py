
self_numbers=set()

#1부터 10000까지 self_number 구하기
for n in range (1,10000):

    num_list=list(map(int,str(n)))
    total=n+sum(num_list)
    if total<=10000:
        self_numbers.add(total)

#1-10000까지 생성된 set에서 self_number 제외 
result=sorted(set([i for i in range(1,10001)])-self_numbers)

#1부터 10000까지 숫자 for문을 돌면서 self_numbers 집합안에 없는 숫자라면 출력하는 방식으로 해도됌!

for r in result:
    print(r)

# 32148	44s

