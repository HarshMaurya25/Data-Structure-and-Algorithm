
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        i = 0
        ans = 0

        for j in range(len(fruits)):
            count[fruits[j]] = count.get(fruits[j], 0) + 1

            while len(count) > 2:
                count[fruits[i]] -= 1

                if count[fruits[i]] == 0:
                    del count[fruits[i]]

                i += 1

            ans = max(ans, j - i + 1)

        return ans

