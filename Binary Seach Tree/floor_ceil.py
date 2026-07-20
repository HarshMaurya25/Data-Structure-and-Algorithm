def floor(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] <= target:
            ans = mid         
            low = mid + 1      
        else:
            high = mid - 1

    return ans

def ceil(arr , target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < target:    
            low = mid + 1      
        else:
            high = mid - 1
            ans = mid     

    return ans

    
arr = [1, 2, 3, 6, 7, 22, 23, 26, 45, 465, 999]

idx = ceil(arr, 9)
print(idx) 