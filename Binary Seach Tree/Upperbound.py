def upperBound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    return low if low < len(arr) else -1

def lowerBound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low if low < len(arr) else -1
    
arr = [1, 2, 2, 2, 2, 2, 2]
print(lowerBound(arr , 2))