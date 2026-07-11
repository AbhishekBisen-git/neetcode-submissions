class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = list(zip(position, speed))
        cars.sort()

        time = [(target - pos) / spd for pos, spd in cars]
                    
        #position = [target-x for x in position]

        #time = [position[i]/speed[i] for i in range(len(position))]   
            
        ctr = 0
        a = 0
        while time  :
            current = time.pop()
            if current > a:
                ctr+=1
                a = current
                
        


        return ctr
            