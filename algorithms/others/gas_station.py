# Gas Station
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# assume the answer is unique, and the input values are non-negative and valid
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) != len(cost) or sum(gas) < sum(cost):
            return -1

        position = 0
        balance = 0  # current tank balance

        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                # journey from last position to i is not possible
                # should be visited during the later part of the entire journey
                balance = 0
                position = i + 1

        return position
# approach:
# 1. prove that if total gas is more than total cost, there must be a solution.
#    (for the station that has greatest negative diff, there must be one or more
#    stations that have a total positive balance greater than that negative dff)
# 2. if the answer is unique, find the last range of journey that has a negative
#    balance, the next index must be solution
