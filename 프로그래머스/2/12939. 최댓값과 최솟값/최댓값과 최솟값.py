def solution(s):
    nums=list(map(int,s.split(' ')))
    print(nums)
    answer = ''
    print()
    return str(min(nums))+' '+str(max(nums))
