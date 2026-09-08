def palindrome(n : int, count : int):
    if(n <= 0):
        return count
    
    if(n % 10 == 0):
        return palindrome(n // 10 , count + 1)
    else:
        return palindrome(n//10 , count)
    

def palindrome2(n : int):
    if(n <= 0):
        return 0
    if(n % 10 == 0):
        return palindrome2(n // 10) + 1
    else:
        return palindrome2(n//10)

print(palindrome2(10203000))