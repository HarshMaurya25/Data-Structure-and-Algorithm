class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            # Find the maximum element in the middle column
            max_row = 0
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            left_val = mat[max_row][mid - 1] if mid > 0 else -1
            right_val = mat[max_row][mid + 1] if mid < n - 1 else -1

            # Peak found
            if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
                return [max_row, mid]

            # Move towards the larger neighbor
            elif left_val > mat[max_row][mid]:
                right = mid - 1
            else:
                left = mid + 1