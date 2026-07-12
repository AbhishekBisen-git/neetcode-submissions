class Solution:
    def search(self, nums: List[int], target: int) -> int:
                
        nums = nums
        target = target

        left = 0
        right = len(nums)-1

        while left <= right:
            m = (left+right)//2

            if nums[m] == target:
                return(m)
                break
            elif nums[m]>target:
                right = m-1
            elif nums[m]<target:
                left = m+1
        
        return(-1)
        