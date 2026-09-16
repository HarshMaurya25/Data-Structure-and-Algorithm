class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])

        for i in strs:
            length = min(length , len(i))

        ans = ""
        for i in range(length):
            letter = strs[0][i]

            for x in strs:
                if x[i] != letter:
                    return ans
            
            ans += letter
        
        return ans