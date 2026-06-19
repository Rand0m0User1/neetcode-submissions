class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        pairs_sorted = sorted(pairs, reverse=True)
        fleets = 0
        max_time = 0.0

        for i in range(len(pairs_sorted)):
            time_to_finish = (target - pairs_sorted[i][0]) / pairs_sorted[i][1]
            # distance/vel = time

            print(time_to_finish)

            if time_to_finish > max_time:
                fleets += 1
                max_time = time_to_finish

        return fleets