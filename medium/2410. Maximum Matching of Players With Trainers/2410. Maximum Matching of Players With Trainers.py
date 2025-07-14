from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        return self.solution1(players, trainers)

    def solution1(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0

        for player in players:
            while trainers and player > trainers[0]:
                trainers.pop(0)

            if trainers and player <= trainers[0]:
                res += 1
                trainers.pop(0)
            else:
                break

        return res

    def solution2(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        player, trainer = 0, 0
        np, nt = len(players), len(trainers)
        res = 0

        while player < np and trainer < nt:
            if players[player] <= trainers[trainer]:
                res += 1
                player += 1
                trainer += 1
            else:
                trainer += 1

        return res
