from collections import Counter

n=int(input())

fruits_dict={}

#순회하면서 카운터
for i in range(n):
    fruit,num=input().split()

    fruits_dict[fruit]=fruits_dict.get(fruit,0)+int(num)

#5가 되면 YES
print('YES' if 5 in fruits_dict.values() else 'NO')
