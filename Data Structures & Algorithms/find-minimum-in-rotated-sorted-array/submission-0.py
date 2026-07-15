class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # Minimum lies on the right side
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is at mid or on the left side
            else:
                right = mid

        return nums[left]