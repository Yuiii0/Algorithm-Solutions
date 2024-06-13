from itertools import combinations                  
import sys                                          
input=sys.stdin.readline                            
                                                    
n=int(input())                                      
num_list=list(range(1,n+1))                         
result=sum(1 for _ in combinations(num_list,5))     
print(result)                                       
                                                    