class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        a , b , c = -1 , -1 , -1

        def function(num , idx):
            mini = 10 ** 5
            
            if a == -1:
                return 0
            if b == -1:
                return 0
            if c == -1:
                return 0
            
            mini = min(a , b, c)
            
            return mini + 1

        for idx, num in enumerate(s):
            if num is 'a':
                a = idx
            elif num is 'b':
                b = idx
            elif num is 'c':
                c = idx

            # print(idx , a , b , c, function(num, idx))
            ans += function(num , idx)

        return ans