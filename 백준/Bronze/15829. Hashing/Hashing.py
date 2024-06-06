import sys
input = sys.stdin.readline

n=int(input())

input_hash={chr(ord('a')+i) :i+1 for i in range(26)}            

s=input()
result=0

for i in range(n):
    str_to_num=input_hash[s[i]]
    result+=str_to_num*(31**i)
print(result)
    
 
        
