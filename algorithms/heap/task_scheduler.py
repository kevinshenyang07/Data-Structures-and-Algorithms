from collections import Counter
from heap import Heap

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
        heap = Heap(lambda t: (-t[1], t[0]))
        for task, cnt in counter.items():
            heap.push((task, cnt))

        # each cycle has n + 1 intervals
        # the idle intervals in last cycle don't count
        cycles = curr_cycle_num_tasks = 0

        while len(heap) > 0:
            cycles += 1
            curr_cycle_num_tasks = min(n + 1, len(heap))
            curr_cycle = []  # tasks that have been scheduled in the cycle

            for _ in range(curr_cycle_num_tasks):
                # fill the cycle with taks of currently largest occurrence
                task, cnt = heap.pop()
                if cnt > 1:
                    curr_cycle.append((task, cnt - 1))

            for pair in curr_cycle:
                heap.push(pair)

        return (n + 1) * (cycles - 1) + curr_cycle_num_tasks


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
