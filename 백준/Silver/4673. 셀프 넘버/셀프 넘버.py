
self_numbers=set()

#1부터 10000까지 self_number 구하기
for n in range (1,10000):

    num_list=list(map(int,str(n)))
    total=n+sum(num_list)
    if total<=10000:
        self_numbers.add(total)
result=sorted(set([i for i in range(1,10001)])-self_numbers)

for r in result:
    print(r)


