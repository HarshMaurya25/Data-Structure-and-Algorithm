class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length == 0:
            return 0

        if length == 1:
            return 1

        words = set()
        i = 0
        j = 0
        ans = 0

        words.add(s[i])

        while j < length:
            # print(ans, s[j], j, s[i], i, words)

            ans = max(ans, len(words))

            if j == length - 1:
                break

            elif s[j + 1] in words:
                words.discard(s[i])

                if i == j:
                    j += 1
                    words.add(s[j])

                i += 1

            else:
                j += 1
                words.add(s[j])

        return ans
