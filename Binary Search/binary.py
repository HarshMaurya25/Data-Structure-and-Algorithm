import bisect
def binarySearch(arr, target):
    low = 0 
    high = len(arr) - 1

    while(low <= high):
        mid = low + (high - low)//2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    
        return -1
    
arr = [1, 2, 3, 6, 7, 22, 23, 26, 45, 465,999]
print(binarySearch(arr , 22))
print(bisect.bisect_left(arr , 22))

