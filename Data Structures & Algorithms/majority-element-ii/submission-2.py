class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:


        
        nums = nums

        d = {}
        l = len(nums)

        for i in range(len(nums)):
            
            if nums[i] not in d:
                d[nums[i]] = 1
            elif nums[i] in d:
                d[nums[i]] += 1
            
        return [x[0] for x in list(d.items()) if x[1] > l/3] if l>1 else nums