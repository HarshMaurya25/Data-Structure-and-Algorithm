class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] ans = new int[nums.length];

        int even = 0;
        int odd = 0;

        for (int num: nums){
            if (num >= 0){
                ans[even * 2] = num;
                even++;
            }else{
                ans[odd * 2 + 1] = num;
                odd++;
            }
        }

        return ans;
    }
}