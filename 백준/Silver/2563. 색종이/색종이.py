#100x100 도화지 2차원 리스트 생성
base=[[0]*100 for _ in range(100)]
n=int(input())

#주어진 x,y값을 순회하면서 도화지 채우기
for _ in range(n):
    x,y=map(int,input().split())
    #10x10 색종이 붙이기
    for dx in range(10):
        for dy in range(10):
            base[x+dx][y+dy]=1 #1로 채우기
            
#base배열 순회하면서 채워진 영역 카운트=sum
print(sum(sum(line) for line in base))
