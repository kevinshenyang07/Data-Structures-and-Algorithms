# Maximum Vacation Days
# Rules:
# 1. You can only travel among N cities, represented by indexes from 0 to N-1.
#    Initially, you are in the city indexed 0 on Monday.
# 2. The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical),
#    called flights representing the airline status from the city i to the city j.
#    If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1.
#    Also, flights[i][i] = 0 for all i.
# 3. You totally have K weeks (each week has 7 days) to travel.
#    You can only take flights at most once per day and can only take flights on each week's Monday morning.
#    Since flight time is so short, we don't consider the impact of flight time.
# 4. For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship.
#    For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.
# You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.
#
# Note:
# 1 <= N, K <= 100
# if you fly from the city A to the city B and take the vacation on that day,
# the deduction towards vacation days will count towards the vacation days of city B in that week.
#
# Example:
# flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]] => 6 + 3 + 3 = 12
# flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]] => 1 + 1 + 1 = 3
# flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]] => 7 + 7 + 7 = 21
class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        dp[i][j]: max number of vacation days taken at the end of week j in city i

        dp[i][j] = -inf                              no flights to city i
                 = days[i][0]                        j == 0 and flights[0][i] == 1
                 = max(dp[k][j - 1] + days[i][j])    j > 0, 0 <= k < N
        """
        N, K = len(days), len(days[0])
        dp = [[float('-inf')] * K for _ in range(N)]  # haven't been able to reach yet
        max_days = 0

        # base cases
        # mind that one can stay at the same city for the upcoming week
        for i in range(N):
            if i == 0 or flights[0][i] == 1:
                dp[i][0] = days[i][0]

        for j in range(1, K):
            for i in range(N):  # dst city
                for k in range(N):  # src city
                    if k == i or flights[k][i] == 1:
                        dp[i][j] = max(dp[i][j], dp[k][j - 1] + days[i][j])
                max_days = max(max_days, dp[i][j])

        return max_days
# O(k * n^2) time, O(n^2) space (can be reduced to O(n)space)
