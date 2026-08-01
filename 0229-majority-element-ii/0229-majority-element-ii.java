class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int num : nums) {
            if (hashmap.containsKey(num)) {
                hashmap.put(num, hashmap.get(num) + 1);
            } else {
                hashmap.put(num, 1);
            }
        }

        ArrayList<Integer> arr = new ArrayList<>();
        hashmap.forEach((key, value) -> {
            if (value > nums.length / 3) {
                arr.add(key);
            }
        });

        return arr;
    }
}