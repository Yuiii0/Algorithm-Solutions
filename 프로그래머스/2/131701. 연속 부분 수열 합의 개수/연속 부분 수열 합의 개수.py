def solution(elements):
    num_set=set(elements)
    answer = 0

    extended_elements = elements * 2

    for n in range(2,len(elements)+1):
        for i in range(len(elements)):
            sub=extended_elements[i:i+n]
            num_set.add(sum(sub))
    answer+=len(num_set)

    return answer

