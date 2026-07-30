class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        nums = heights
        left = 0
        v = 0
        right = len(nums)-1
        

        while right != left :

            if (right-left)*min(nums[right],nums[left])>v:
                v = (right-left)*min(nums[right],nums[left])
                if nums[right]>nums[left]:
                    left+=1
                else:
                    right-=1

            elif (right-left)*min(nums[right],nums[left])<=v:

                if nums[right]>nums[left]:
                    left+=1
                else:
                    right-=1



        return v