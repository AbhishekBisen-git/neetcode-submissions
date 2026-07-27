class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        d = {}

        for right in range(len(nums)):
            if nums[right] in d:
                return True
            else:
                d[nums[right]] = right
        return False