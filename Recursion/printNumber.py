def ascending(n : int):
    if(n > 10):
        return
    print(n)
    ascending(n+1)

def descending(n : int):
    if(n > 10):
        return
    descending(n+1)
    print(n)
    

ascending(0)
descending(0)

