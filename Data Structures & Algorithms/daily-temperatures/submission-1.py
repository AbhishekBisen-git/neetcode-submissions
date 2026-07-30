class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        nums = temperatures
        l = len(nums)*[0]
        st = []


        for right in range(len(nums)):
            
            while  st and nums[right]>st[-1][0]   :
                temp,index = st.pop()
                #print(right)
                l[index] = right - index
                
            st.append(tuple([nums[right],right]))
        return l