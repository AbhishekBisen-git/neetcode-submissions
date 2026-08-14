
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = nums
        target = target
        d = {}

        for i in range(len(nums)):
            if target-nums[i] in d:
                return([d[target-nums[i]],i])
            elif nums[i] not in d:
                d[nums[i]] = i
                    