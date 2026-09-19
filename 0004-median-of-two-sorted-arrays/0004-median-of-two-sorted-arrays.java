class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int[] n1, n2;
        if (nums1.length < nums2.length) {
            n1 = nums1;
            n2 = nums2;
        } else {
            n1 = nums2;
            n2 = nums1;
        }

        int l1 = n1.length;
        int l2 = n2.length;

        int answer = 0;

        int low = 0;
        int high = l1;

        while (low <= high) {
            int mid1 = (low + high) / 2;
            int mid2 = (l1 + l2 + 1) / 2 - mid1;

            int low1, low2, high1, high2;

            low1 = (mid1 <= 0) ? Integer.MIN_VALUE : n1[mid1 - 1];
            low2 = (mid2 <= 0) ? Integer.MIN_VALUE : n2[mid2 - 1];
            high1 = (mid1 >= l1) ? Integer.MAX_VALUE : n1[mid1];
            high2 = (mid2 == l2) ? Integer.MAX_VALUE : n2[mid2];

            if (low1 <= high2 && low2 <= high1) {
                if ((l1 + l2) % 2 == 0) {
                    System.out.println(String.format("%d %d and %d %d%n %d + %d",
                            low1,
                            low2,
                            high1,
                            high2,
                            Math.max(low1, low2),
                            Math.min(high1, high2)));
                    return (double)(Math.max(low1, low2) + Math.min(high1, high2)) / 2;
                } else {
                    return Math.max(low1, low2);
                }
            } else if (low1 > high2) {
                high = mid1 - 1;
            } else {
                low = mid1 + 1;
            }
        }
        return 0;

    }
}