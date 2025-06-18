# Last updated: 6/17/2025, 10:35:10 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        len_column = len(matrix[0])
        len_row = len(matrix)
        left = 0
        right = len_row * len_column - 1
       
        while left <= right: # make it 1D
            mid = (left+right)//2
            row = mid // len_column # make it 2D
            column = mid % len_column # make it 2D
            num = matrix[row][column] #back to 1D

            if num == target:
                return True
            elif num < target:
                left = mid+1
            elif num > target:
                right = mid-1
        return False
