def isPrime(n):
    isPrime = True
    if n > 2 and (n % 2 != 0):
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                isPrime = False
                break
    elif n == 2:
        pass
    else:
        isPrime = False
    
    return isPrime


#Driver Code
""" the firsts 100 primes numbers """
lst = []
primes_numbers = 0
n = 2
while primes_numbers <= 100:
    if isPrime(n): 
        lst.append(n)
        primes_numbers += 1
    n += 1
print(lst)