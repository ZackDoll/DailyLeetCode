class Solution:
    #"Remove" that coin’s contribution by doing,
    #for each s from c up to n: numWays[s] -= numWays[s - c]
    def findCoins(self, numWays: List[int]) -> List[int]:
        denoms = []
        curr_value = 0
        n = len(numWays)

        for i in range(len(numWays)):
            if numWays[i] == 1:
                curr_value = i + 1
                denoms.append(curr_value)

                for j in range(n-1, curr_value - 1, -1):
                    numWays[j] -= numWays[j-curr_value]
                numWays[i] = 0

        for i in range(n):
            if numWays[i] != 0:
                return []
        return denoms
