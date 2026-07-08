class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = s1
        s2 = s2
        k = len(s1)
        left = 0

        d1 = {}
        d2 = {}
        for i in range(len((s1))):
            if s1[i] in d1:
                d1[s1[i]]+=1
            elif s1[i] not in d1:
                d1[s1[i]]=1
                
            
        for right in range(len(s2)):
            
            if s2[right] in d2:
                d2[s2[right]]+=1
            elif s2[right] not in d2:
                d2[s2[right]]=1
            
            if d1==d2:
                return True
            
            while right - left+1 >k:
                
                if d2[s2[left]]==1:
                    d2.pop(s2[left])
                else:
                    d2[s2[left]]-=1
                    
                left+=1
                if d2 == d1:
                    return True
        return False
        
    
        