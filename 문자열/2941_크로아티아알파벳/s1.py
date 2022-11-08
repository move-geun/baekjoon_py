base = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()
for n in base:
    N = N.replace(n, 'a')
print(len(N))