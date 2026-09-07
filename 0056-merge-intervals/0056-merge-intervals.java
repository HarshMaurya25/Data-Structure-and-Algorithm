class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (x, y) -> Integer.compare(x[0], y[0]));

        ArrayList<int[]> ans = new ArrayList<>();

        Arrays.stream(intervals).forEach(interval -> {
            if (ans.isEmpty() || interval[0] > ans.get(ans.size() - 1)[1]) {
                ans.add(interval);
            } else {
                ans.get(ans.size() - 1)[1] =
                    Math.max(ans.get(ans.size() - 1)[1], interval[1]);
            }
        });

        return ans.toArray(new int[ans.size()][]);
    }
}
