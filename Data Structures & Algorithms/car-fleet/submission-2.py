class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the cars by position from closest to farthest (relative to target)
        cars = sorted(zip(position,speed), reverse = True)

        fleets = 0
        last_arrival_time = 0 # time of fleet ahead

        for pos, spd in cars:
            arrival_time = (target-pos)/spd

            # if the current car arrives later than the fleet ahead
            # then it forms a new fleet
            if arrival_time > last_arrival_time:
                last_arrival_time = arrival_time
                fleets += 1
        
        return fleets



