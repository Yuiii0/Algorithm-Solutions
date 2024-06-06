#31120	44

import sys
s=sys.stdin.readline()

#10간격으로 출력
for i in range(0,len(s),10):
    print(s[i:i+10])