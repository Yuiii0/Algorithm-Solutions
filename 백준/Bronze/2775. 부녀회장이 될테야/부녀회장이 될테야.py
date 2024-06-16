import sys
input=sys.stdin.readline

tc=int(input())




def make_apartment_table(k,n):
    #k-1층의 n호까지의 합
    #0층의 n호까지
    apartment[0]=list(range(n+1))
    for i in range(1,k+1):
        for j in range(n+1):
            apartment[i][j] = sum(apartment[i - 1][:j + 1])
        # print(i)
        #k-1층, n호까지 apartment dp 구하기
        # print('sum을 위한 slicing',apartment[i-1][:n+1])
        # print(sum(apartment[i-1][:n+1]))

    return apartment[k][n]




for _ in range(tc):
    k=int(input())
    n=int(input())
    apartment = [[0] * (n + 1) for _ in range(k+1)]
    result=make_apartment_table(k,n)
    print(result)

