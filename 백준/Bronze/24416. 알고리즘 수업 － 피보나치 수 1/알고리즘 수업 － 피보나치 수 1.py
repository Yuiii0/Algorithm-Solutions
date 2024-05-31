n=int(input())

def fib_recursion(n):
    #배열 생성
    fib_list =[0]*(n + 1)
    fib_list[1]=1
    fib_list[2]=1
    
    if n==1 or n==2:
        return 1
        
    for i in range(3,n+1):
        fib_list[i]=fib_list[i-1]+fib_list[i-2]

    return fib_list[n]

def fib_dinamic(n):
    return n-2 

print(fib_recursion(n),fib_dinamic(n))

