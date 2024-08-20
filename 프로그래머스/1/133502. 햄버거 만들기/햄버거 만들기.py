def solution(ingredient):
    answer = 0
    target=[1,2,3,1]
    stack=[]

    for num in ingredient:
        stack.append(num)

        if stack[-4:] == target:
            answer+=1
            for _ in range(4):
                stack.pop()

    return answer