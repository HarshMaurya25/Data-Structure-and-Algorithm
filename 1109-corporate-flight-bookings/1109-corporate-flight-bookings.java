class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] diff = new int[n + 1];

        for (int[] b : bookings) {
            int start = b[0] - 1;
            int end = b[1];
            int seats = b[2];

            diff[start] += seats;
            diff[end] -= seats;
        }

        int[] ans = new int[n];
        int current = 0;

        for (int i = 0; i < n; i++) {
            current += diff[i];
            ans[i] = current;
        }

        return ans;
    }
}
