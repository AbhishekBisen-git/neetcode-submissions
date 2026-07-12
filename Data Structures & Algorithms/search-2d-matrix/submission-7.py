class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nums = matrix
        target = target

        left = 0
        right = len(nums)*len(nums[0])-1
        l = len(nums[0])
        r = len(nums)

        while left<=right :
            
            mid = (left+right)//2
            row = mid%l
            col = mid//l

            
            if nums[col][row] == target:
                return True
                break
            elif nums[col][row] > target:
                right = mid-1
            elif nums[col][row] < target:
                left = mid+1
                
        return False
    