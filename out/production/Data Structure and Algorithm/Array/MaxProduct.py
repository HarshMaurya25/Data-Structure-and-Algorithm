class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        max1 = 0 
        max2 = 0

        for x in n:
            i = int(x)
            if max1 <= i:
                max2 = max1 
                max1 = i
            else:
                if max2 <= i:
                    max2 = i
            
            print(i , max1 , max2)

        
        return max1 * max2