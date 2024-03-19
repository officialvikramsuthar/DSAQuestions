def is_palindrome(num):

    reverse = 0
    temp = num 

    while num > 0 :
        remainder = num % 10 
        num = num // 10 
        reverse = reverse * 10 + remainder

    return reverse == temp

print(is_palindrome(-121))