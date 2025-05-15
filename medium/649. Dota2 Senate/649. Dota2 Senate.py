from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # t = {"R": "Radiant", "D": "Dire"}

        # if len(senate) == 1:
        #     return t[senate[0]]

        # queue = list(senate)

        # while queue != 1:
        #     curr = queue.pop(0)

        #     for i in range(len(queue)):
        #         if curr != queue[i]:
        #             queue.pop(i)
        #             queue.append(curr)
        #             break

        #     if not queue:
        #         return t[curr]

        # return t[queue[0]]

        r_queue = deque()
        d_queue = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while d_queue and r_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()

            if r < d:
                r_queue.append(r + n)
            else:
                d_queue.append(d + n)

        return "Radiant" if r_queue else "Dire"


solution = Solution()
print(solution.predictPartyVictory(senate="RD"))
print(solution.predictPartyVictory(senate="RDD"))
print(solution.predictPartyVictory(senate="R"))
print(
    solution.predictPartyVictory(
        senate="RRDRDRDRDRDRRRDRRDRDRDRDRDRDRDRDRRDRDDDDDDDRDRRDRDRDRRD"
    )
)
print(solution.predictPartyVictory(senate="DRRDRDRDRDDRDRDR"))
print(solution.predictPartyVictory(senate="DDRRR"))
