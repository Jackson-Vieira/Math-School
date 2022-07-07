def mdc(a, b):
    while b: # b != 0
        a, b = b, a % b
    return a


print(mdc(3, 2)) 


