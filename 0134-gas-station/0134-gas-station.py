class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        start = 0
        tank = 0
        total = 0
        
        for i in range(n):
            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1



