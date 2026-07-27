class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for right in range(len(nums)):

            if target - nums[right] in d:
                return ([d[target - nums[right]],right])
            else :
                d[nums[right]] = right