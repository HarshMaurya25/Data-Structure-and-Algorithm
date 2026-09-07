class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * 1001

        for people, start, end in trips:
            prefix[start] += people
            prefix[end] -= people

        current = 0

        for change in prefix:
            current += change

            if current > capacity:
                return False

        return True
