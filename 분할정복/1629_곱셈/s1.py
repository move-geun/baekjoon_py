# import sys

# A,B,C = map(int, sys.stdin.readline().split())
# tmp = A
# for i in range(1,B+1):
#     if tmp < C:
#         tmp **= i
#     elif tmp > C:
#         tmp %= C

# print(tmp)

import sys
a,b,c = map(int,sys.stdin.readline().split())

def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
          
print(multi(a,b))