class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        ans = s

        for i in range(len(nums)-k):
            s = s - nums[i]+nums[i+k]
            ans = max(ans,s)
        return ans/k
