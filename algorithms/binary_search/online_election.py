# Online Election
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        votes = {}
        curr_leader = None

        for i in range(len(persons)):
            person, time = persons[i], times[i]
            votes[person] = votes.get(person, 0) + 1

            if votes[person] >= votes.get(curr_leader, 0):
                curr_leader = person
            self.leaders.append(curr_leader)

    # be careful that t could be >= times[-1]
    def q(self, t):
        left, right = 0, len(self.times) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if self.times[mid] < t:
                left = mid
            elif self.times[mid] > t:
                right = mid
            else:
                return self.leaders[mid]

        if self.times[right] <= t:
            return self.leaders[right]
        else:
            return self.leaders[left]
# O(n) time and space for init, O(logn) for query
# can pre-compute the results to improve query performance, but could take large space
