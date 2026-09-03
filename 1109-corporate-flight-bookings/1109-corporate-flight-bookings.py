class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)

        for l, r, seats in bookings:
            diff[l - 1] += seats
            diff[r] -= seats

        ans = [0] * n
        curr = 0

        print(diff)

        for i in range(n):
            curr += diff[i]
            ans[i] = curr

        return ans