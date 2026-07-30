class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(s.split()).lower()
        left = 0
        right = len(s)-1

        while left<=right:

            if s[right].isalnum()==1 and s[left].isalnum()==1:
                if s[left].lower() != s[right].lower():
                    return(False)
                elif s[left].lower() == s[right].lower():
                    left+=1
                    right-=1
                
            elif s[right].isalnum() !=1:
                right-=1
            elif s[left].isalnum() !=1:
                left+=1
        return(True)