class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        for i in range(len(position)):

            for j in range(len(position)):

                if position[i]<position[j]:
                    position[i],position[j] = position[j],position[i]
                    speed[i],speed[j] = speed[j],speed[i]
                    
        position = [target-x for x in position]

        time = [position[i]/speed[i] for i in range(len(position))]   
            
        ctr = 0
        a = 0
        while time  :
            current = time.pop()
            if current > a:
                ctr+=1
                a = current
                
        


        return ctr
            