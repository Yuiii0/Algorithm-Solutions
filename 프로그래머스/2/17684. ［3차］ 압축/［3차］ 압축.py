def solution(msg):
    answer = []
    dictionary = {}

    for x in range(65, 91):
        char = chr(x)
        index = x - 64
        dictionary[char] = index

    idx_f, idx_e = 0, 0

    while True:
        idx_e += 1
        if idx_e == len(msg):
            answer.append(dictionary[msg[idx_f:idx_e]])
            break

        if msg[idx_f:idx_e + 1] not in dictionary.keys():
            dictionary[msg[idx_f:idx_e + 1]] = len(dictionary) + 1
            answer.append(dictionary[msg[idx_f:idx_e]])
            idx_f = idx_e
            
    return answer