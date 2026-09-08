class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        codematch = {
            "2" : "abc", 
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        answerList = []
        def solution(i , answer):
            if(i == len(digits)):
                answerList.append("".join(answer[:]))
                return 
            
            num = digits[i]
            for a in codematch[num]:
                answer.append(a)
                solution(i + 1, answer)
                answer.pop()
        
        solution(0 , [])
        return answerList
        