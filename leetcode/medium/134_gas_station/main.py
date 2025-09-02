class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g = sum(gas)
        c = sum(cost)

        if c > g: return -1

        current = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            
            current += diff
            if current < 0:
                current = 0
                start = i + 1
        return start
        
