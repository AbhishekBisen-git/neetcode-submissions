class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s = s
        k = k
        d = {}
        left = 0
        l = 0
        for right in range(len(s)):
            
            if s[right] not in d:
                d[s[right]] = 1
            elif s[right] in d:
                d[s[right]]+=1
                
            max_value = max(d.values())
            
            
            while right-left+1-max_value>k:
                d[s[left]] -= 1
                left+=1
                
            l = max(l,right-left+1)
        return l