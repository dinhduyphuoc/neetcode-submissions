class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        maxTime = 0
        for pos, spd in cars:
            t = (target - pos) / spd
            if t > maxTime:
                fleets += 1
                maxTime = t

        return fleets