class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def checking(s):
            i = 0
            j = len(s) - 1
            while(j > i):
                if(s[i] != s[j]):
                    return False
                i += 1
                j -= 1
            return True
        
        def backtracking(s , partition):
            if(len(s) == 0 ):
                answer.append(partition[:])
                return
            
            for i in range(0 , len(s)):
                part = s[0:i+1]

                if(checking(part) is False):
                    continue

                partition.append(part)
                backtracking(s[i+1:] , partition)
                partition.pop()
        
        backtracking(s , [])
        return answer




        