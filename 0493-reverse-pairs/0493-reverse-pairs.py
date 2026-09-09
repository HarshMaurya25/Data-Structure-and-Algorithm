class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def mergeSort(nums, start , end, count):
            if end - start <= 1:
                return count

            mid = (start + end)//2

            count = mergeSort(nums, start , mid, count)
            count = mergeSort(nums, mid , end, count)

            return merge(nums , start , mid , end, count)
        
        def merge(nums , start , mid , end, count):
            newNum = []
            for i in range(start, mid):
                low = mid
                high = end

                while low < high:
                    m = (low + high) // 2

                    if nums[m] * 2 < nums[i]:
                        low = m + 1
                    else:
                        high = m

                count += low - mid

            
            i = start
            j = mid

            while i < mid and j < end:
                if nums[i] < nums[j]:
                    newNum.append(nums[i])
                    i += 1
                else:
                    newNum.append(nums[j])
                    j+=1
            
            while i < mid:
                newNum.append(nums[i])
                i += 1
            
            while j < end:
                newNum.append(nums[j])
                j += 1
        
            for i in range(len(newNum)):
                nums[start + i] = newNum[i]

            
            return count

        return mergeSort(nums , 0 , len(nums), 0)