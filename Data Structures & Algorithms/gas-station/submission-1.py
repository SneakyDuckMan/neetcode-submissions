class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i]- cost[i] for i in range(len(gas))]

        if sum(gas) < sum(cost):
            return -1

        curr_sum = 0
        ans = 0

        for i, gas in enumerate(diff):
            curr_sum += gas

            if curr_sum < 0:
                curr_sum = 0
                ans = i + 1
            
        return ans