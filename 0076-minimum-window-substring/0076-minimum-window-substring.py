class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        have = {}
        
        left = 0
        formed = 0
        required = len(need)

        ans = ""
        min_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    ans = s[left:right + 1]

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return ans
