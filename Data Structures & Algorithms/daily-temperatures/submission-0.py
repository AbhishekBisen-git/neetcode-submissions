class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        nums = temperatures
        st = [0]* len(nums)
        q = []


        for i in range(len(nums)):
            
            while q and nums[q[-1]] < nums[i]:
                st[q[-1]] = i-q[-1]
                q.pop()
                
            
            q.append(i)
        return st