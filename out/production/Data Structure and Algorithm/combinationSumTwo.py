class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answerList = []

        def solution(count, i , answer):
            if(count == k):
                if(sum(answer) == n):
                    print("Seven")
                    answerList.append(answer[:])
                return
            

            while( i <= 9 ):
                
                if((sum(answer) + i) <= n):
                    answer.append(i)
                    print(answer , k , count)
                    solution(count + 1 , i + 1 , answer)
                    answer.pop()
                i+=1
        
        solution(0 , 1 , [])
        return answerList