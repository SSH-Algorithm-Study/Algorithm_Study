class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        first_m, first_n = 0, 0
        last_m, last_n = m - 1, n - 1

        while first_m <= last_m and first_n <= last_n:
            mid_m, mid_n = first_m + (last_m - first_m) // 2, first_n + (last_n - first_n) // 2

            if matrix[mid_m][mid_n] == target:
                return True

            elif matrix[mid_m][mid_n] > target:
                if mid_m - 1 < 0 :
                    last_m, last_n = mid_m, mid_n - 1
                elif mid_n -1 < 0 :
                    last_m, last_n = mid_m - 1, mid_n
                elif matrix[mid_m - 1][mid_n] > matrix[mid_m][mid_n - 1]:
                    last_m, last_n = mid_m - 1, mid_n
                else:
                    last_m, last_n = mid_m, mid_n - 1

            else:
                if mid_m + 1 > last_m:
                    first_m, first_n = mid_m, mid_n + 1
                elif mid_n + 1 > last_n:
                    first_m, first_n = mid_m + 1, mid_n
                elif matrix[mid_m + 1][mid_n] < matrix[mid_m][mid_n + 1]:
                    first_m, first_n = mid_m + 1, mid_n
                else:
                    first_m, first_n = mid_m, mid_n + 1

        return False





