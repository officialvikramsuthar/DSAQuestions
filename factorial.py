# a = 0 
# b = 1

# print(a)
# print(b)
# n = 6

# for i in range(2, n):
#     sum = a + b
#     a = b
#     b = sum
#     print(sum)

def factorial(n):
    print(n)

    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n-1)