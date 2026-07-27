class Solution:
    def binary_search(self,arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target: return mid
            elif arr[mid] < target: left = mid + 1
            else: right = mid - 1
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0]==target:
            return True
        for i in range(len(matrix)):
            if matrix[i][-1]>=target:
                if self.binary_search(matrix[i],target)!=-1:
                    return True
        
        return False