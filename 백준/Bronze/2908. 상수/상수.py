#두 숫자를 뒤집어서 숫자 비교

num1,num2=input().split()
print(max(num1[::-1],num2[::-1]))
