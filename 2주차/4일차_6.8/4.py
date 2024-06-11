import sys

# 올바르지 않은 괄호 개수 파악
# 짝이 맞지 않는 ) 개수 카운트
# 스택에 남아 있는 ( 개수 카운트



def find_unmatched_brackets(brackets):
    stack=[]
    count=0 #올바르지 않은 괄호 개수
    for bracket in brackets:
        if bracket=='(':
            stack.append(bracket)
        else:
            # 짝지을 왼쪽 괄호가 있다면 pop
            if stack:
                stack.pop()
            # 짝지을 왼쪽 괄호가 없다면 count
            else:
                count+=1
    # 짝이 맞지 않아 남은 괄호 개수
    count+=len(stack)
    return count

def read_input():
    input = sys.stdin.readline
    brackets= input().strip()
    return brackets

def main():
    brackets=read_input()
    result=find_unmatched_brackets(brackets)
    print(result)





if __name__ == "__main__":
    main()


#31120	44