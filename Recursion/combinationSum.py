class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        current = []

        def solution(candidates, current):
            if sum(current) == target:
                temp = current.copy()
                temp.sort()
                if temp not in answer:
                    answer.append(temp)
                return
            elif sum(current) > target:
                return

            for i in candidates:
                current.append(i)
                solution(candidates, current)
                current.pop()

        solution(candidates , current)
        return answer


        