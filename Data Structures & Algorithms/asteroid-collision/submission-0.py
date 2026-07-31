class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st = []
        nums = asteroids




        for i in range(len(nums)):

            
            if st and (st[-1]>0 and nums[i]<0):
                while st and abs(st[-1])<abs(nums[i]) and  st[-1] > 0 and nums[i] < 0:
                    st.pop()
        
        
            
                    
            if st and (st[-1]>0 and nums[i]<0) and abs(st[-1]) > abs(nums[i]):
                continue
            elif st and (st[-1]>0 and nums[i]<0) and abs(st[-1])==abs(nums[i]):
                st.pop()
            else:
                st.append(nums[i])
        return st