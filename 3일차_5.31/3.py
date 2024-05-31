n=int(input())

total=0
temp=0

#i=1 -> 5+4+3+2+1
#i=2 -> 4+3+2+1
#i=3 -> 3+2+1
#i=4 -> 2+1
#i=5 -> 1

for i in range(1,n-1): 
    temp=temp+i #1 3 6 10 15
    total+=temp 
    

print(total) #순회 횟수
print(3) #삼중 for문 O(n^3)