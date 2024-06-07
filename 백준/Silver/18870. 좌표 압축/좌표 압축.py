import sys

def create_dict(num_set):
    dict = {}
    for i, num in enumerate(sorted(list(num_set))):
        if not num in dict:
            dict[num] = i
    return dict
#
def find_idx(num_list,dict):
    result=[str(dict[num]) for num in num_list ]
    return ' '.join(result)


def read_input():
    input = sys.stdin.readline
    n = int(input())
    num_list = list(map(int, input().split()))
    num_set = set(num_list)
    return num_list,num_set

def main():
    num_list,num_set=read_input()
    dict=create_dict(num_set)
    result=find_idx(num_list,dict)
    print(result)


if __name__ == "__main__":
    main()