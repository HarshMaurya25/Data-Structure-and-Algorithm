class Solution:
    def maximumWidth(self, planks: list[int]) -> int:

        planks.sort()
        lastpos = 0

        def maxPlank(x, lastpos):
            avoid = set()

            for pos in range(lastpos, len(planks)):
                if planks[pos] == x:
                    avoid.add(pos)
                else:
                    lastpos = pos
                    break

            i = 0
            j = len(planks) - 1

            ans = len(avoid)

            while i < j:
                while i in avoid:
                    i += 1
                while j in avoid:
                    j -= 1

                if i >= j:
                    break

                if planks[i] + planks[j] == x:
                    i += 1
                    j -= 1
                    ans += 1
                elif planks[i] + planks[j] < x:
                    i += 1
                else:
                    j -= 1

            return [ans, lastpos]

        possible = set(planks)
        n = len(planks)

        for i in range(n):
            for j in range(i + 1, n):
                possible.add(planks[i] + planks[j])

        ans = 0
        for width in sorted(possible):
            value = maxPlank(width, lastpos)
            lastpos = value[1]
            ans = max(ans, value[0])

        return ans


s = Solution()
i = [1,3,2,5,7,5,4,2,1]
print("Answer is : ",s.maximumWidth(i))
        
