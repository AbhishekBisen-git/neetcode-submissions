class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        
        nums = numbers
        target = target
        d={}


        for right in range(len(nums)):
    
    
            if target-nums[right]  in d:
                return( [ d[target-nums[right]]+1,right+1 ] )
            
            elif nums[right] not in d:
                d[nums[right]] = right


