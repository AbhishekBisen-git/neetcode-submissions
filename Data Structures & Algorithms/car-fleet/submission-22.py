class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        target = target
        position = position
        speed = speed

        position = [target-x for x in position]



        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        position = [p for p, s in cars]
        speed = [s for p, s in cars]
                

        time = [position[i]/speed[i] for i in range(len(position))]


        ctr = 0
        while time:
            a = time.pop()
            while time and a>=time[-1]:
                time.pop()
            ctr+=1
        
        return ctr
        
    

