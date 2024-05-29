n,target=map(int,input().split())

nation_list=[]

#sorting하기 위해 이중 리스트로
for i in range(n):
    nation_list.append(list(map(int, input().split())))

#금-은-동 순서대로 sort
nation_list=sorted(nation_list,key=lambda x:(-x[1],-x[2],-x[3]))


rank=1 #1등이 target인 경우 대비 초기값 1로

#리스트 순회하면서,동점여부를 확인하기 위해 이전등수와 비교
#중복x = rank i로 업데이트
#중복= rank 그대로
for i in range(n):
    if i>0 and (nation_list[i][1:]!=nation_list[i-1][1:]): #중복x
        rank=i+1
    #target 발견
    if nation_list[i][0]==target:
        print(rank)
        break