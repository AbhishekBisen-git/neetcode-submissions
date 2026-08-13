class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    


        l = max(weights)
        r = sum(weights)
        w = sum(weights)

        while l<r:
            mid = (l+r)//2
            t_w = 0
            day=1
            
            for i in weights:
                t_w+=i
                
                if t_w>mid:
                    day+=1
                    t_w = i
            
            if day>days:
                l = mid+1
            else:
                r = mid

        return(l)