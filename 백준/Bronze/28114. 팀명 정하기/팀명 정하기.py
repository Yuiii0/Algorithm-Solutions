import sys

def first_naming(years):
    years.sort()
    result = ''.join(map(str, years))
    return result

def sec_naming(sol_name):
    sol_name.sort(key=lambda x: -int(x[0]))
    result = ''.join([t[1][0] for t in sol_name])
    return result

def read_input():
    input = sys.stdin.readline
    year_list = []
    sol_name = []
    for _ in range(3):
        sol, year, name = input().rstrip().split()
        year_list.append(int(year) % 100)
        sol_name.append((sol, name))
    return year_list, sol_name

def main():
    year_list, sol_name = read_input()
    res1 = first_naming(year_list)
    res2 = sec_naming(sol_name)
    print(res1)
    print(res2)

if __name__ == "__main__":
    main()
