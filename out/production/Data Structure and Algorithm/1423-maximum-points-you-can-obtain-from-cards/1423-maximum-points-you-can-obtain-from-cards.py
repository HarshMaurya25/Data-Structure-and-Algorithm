class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum = 0 
        ans = 0 
        j = k - 1

        for i in range(k):
            sum += cardPoints[i]
        
        ans = sum
        i = 1
        while j >= 0:
            sum -= cardPoints[j]
            sum = sum + cardPoints[-i]
            ans = max(sum , ans)
            j -= 1
            i += 1
        
        return ans