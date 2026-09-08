def reverse_number(n):
    if(n <= 0):
        return 0

    return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse_number(n // 10)

print(reverse_number(1234)) 
