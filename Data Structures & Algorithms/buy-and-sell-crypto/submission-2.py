class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        left = 0
        l = 0

        for right in range(len(nums)):

            while nums[right]-nums[left]<0:
                left+=1

            l = max(nums[right]-nums[left],l)

        return l
            