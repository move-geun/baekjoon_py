lst = [input().strip() for _ in range(3)]

for i,l in enumerate(lst):
    if l.isdigit():
        value = int(l)
        idx = i
        break

tmp = value + (3-idx)

if tmp%15 ==0 :
    print('FizzBuzz')
elif tmp%3==0:
    print('Fizz')
elif tmp%5==0:
    print('Buzz')
else:
    print(tmp)