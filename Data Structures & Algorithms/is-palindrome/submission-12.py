class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(' ','').lower()

        for i in s:
            if not i.isalnum():
                s = s.replace(i,'')
                
        lp = 0
        hp = len(s) -1 


        while hp >=lp:
            if s[lp]!=s[hp]:
                return False 
            else:
                lp+=1
                hp-=1
                
        return True