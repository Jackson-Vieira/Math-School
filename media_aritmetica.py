# Solution
def media(*notas):
    return f"{sum(notas)/len(notas):.3f}"

# Driver code
print(media(5,5,5,5))
print(media(5,2,8))
print(media(10,50,70))