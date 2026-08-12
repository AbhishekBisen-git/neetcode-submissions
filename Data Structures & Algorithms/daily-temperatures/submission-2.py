class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        nums = temperatures
        l = [0]*len(nums)
        st = []
        v=()
        for i in range(len(nums)):

            while st and st[-1][0]<nums[i]:
                v = st.pop()
                l[v[1]] = i-v[1] 
            st.append(tuple([nums[i],i]))
        return l