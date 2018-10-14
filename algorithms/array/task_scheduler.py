from collections import Counter
from heapq import heappush, heappop


# Task Scheduler
# Given a char array representing tasks CPU need to do.
# It contains capital letters A to Z where different letters represent different tasks.
# Tasks could be done without original order. Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.
# However, there is a non-negative cooling interval n that means between two same tasks,
# there must be at least n intervals that CPU are doing different tasks or just be idle.
# Return the least number of intervals the CPU will take to finish all the given tasks.
# Example:
# tasks = ["A","A","A","B","B","B"], n = 2
# => 8 (A -> B -> idle -> A -> B -> idle -> A -> B)

# counter => heap
class SolutionV1(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        pq = []
        for k, v in counter.iteritems():
            heappush(pq, (-v, k))

        # with tasks from biggest occurrences to smallest
        intervals_last_cycle = 0
        while pq:
            cycles += 1
            intervals_last_cycle = min(n + 1, len(pq))
            curr_cycle = []  # tasks that have been scheduled in the cycle

            for _ in range(intervals_last_cycle):
                # fill the cycle with taks of currently largest occurrence
                neg_cnt, k = heappop(pq)
                if neg_cnt < -1:
                    curr_cycle.append((neg_cnt + 1, k))

            for pair in curr_cycle:
                heappush(pq, pair)

        return (n + 1) * (cycles - 1) + intervals_last_cycle


# greedy solution, hard to prove, not recommended
class SolutionV2(object):
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        # count number of tasks with largest occurrence
        counts = counter.values()
        max_cnt = max(counts)
        num_tasks_max_cnt = counts.count(max_cnt)
        # least Interval must be >= len(tasks)
        return max(len(tasks), (n + 1) * (max_cnt - 1) + num_tasks_max_cnt )
