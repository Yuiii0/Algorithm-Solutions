                                 
import sys                       
input=sys.stdin.readline         
                                 
n=int(input())                   
                                 
def factorial(n):                
    if n==1:                     
        return 1                 
    return n*factorial(n-1)      
                                 
result=factorial(n)              
print(result)                    
                                 