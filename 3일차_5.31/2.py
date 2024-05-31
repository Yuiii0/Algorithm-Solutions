n=int(input())

#1부터 n-1까지 sum
print(sum([i for i in range(1,n)]))
print(2) #시간복잡도 이중 for문 = O(n^2)