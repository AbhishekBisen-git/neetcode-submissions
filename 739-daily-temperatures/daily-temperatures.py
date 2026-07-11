class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        nums = temperatures

        st = []
        l = [0]*len(nums)

        for right in range(len(nums)):


            while st and nums[right] > st[-1][0]:

                l[st[-1][1]] = right - st[-1][1]

                st.pop()

            st.append(tuple([nums[right],right]))

        return(l)