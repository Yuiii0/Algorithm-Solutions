import sys
input = sys.stdin.readline

year_list=[]
sol_name=[]
# 첫번재 방법
for _ in range(3):
        sol, year, name = input().rstrip().split()
        year_list.append(int(year)%100)
        sol_name.append((sol,name))
year_list.sort()
print(''.join(map(str,year_list)))



# 두번째 방법
sol_name.sort(key=lambda x:-int(x[0]))
for t in sol_name:
    print(t[1][0],end='')



        
        


    