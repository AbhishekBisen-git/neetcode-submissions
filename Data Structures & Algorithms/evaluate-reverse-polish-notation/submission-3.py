class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        nums = tokens
        st = []

        for right in range(len(nums)):
            if nums[right] in ('+','-','*','/') :
                
                if nums[right] == '+':
                    
                    val1= int(st.pop())
                    val2 = int(st.pop())
                    
                    st.append(val1+val2)
                    
                elif nums[right] ==  '-':
                    
                    val1= int(st.pop())
                    val2 = int(st.pop())
                    
                    st.append(val2-val1)
                    
                elif nums[right]== '*':
                    
                    val1 = int(st.pop())
                    val2 = int(st.pop())
                    
                    st.append(val1*val2)
                
                elif nums[right] =='/':
                    
                    val1 = int(st.pop())
                    val2 = int(st.pop())
                    
                    st.append(int(val2/val1))
                    
            else:
                st.append(int(nums[right]))
                
        return(int(st[-1]))
