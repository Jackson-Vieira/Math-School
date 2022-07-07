N = 10

# Solution 01
fibs = [1,1]

for i in range(2,N):
    fibs.append(fibs[i-1]+fibs[i-2])

print(fibs)

# Solution 02
a = 1
b = 0
c = a

for i in range(N):
    print(a, end=" ")
    c = a
    a += b
    b = c