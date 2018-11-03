# Bus Routes
# each routes[i] is a bus route that the i-th bus repeats forever
# we start at bus stop S and we want to go to bus stop T
# rravelling by buses only, find the least number of buses to take
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stop_to_routes = collections.defaultdict(set)

        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_stops = set([S])
        visited_routes = set()
        queue = collections.deque([(S, 0)])

        while queue:
            stop, num_bus = queue.popleft()

            if stop == T:
                return num_bus

            for route_id in stop_to_routes[stop]:
                if route_id not in visited_routes:

                    for next_stop in routes[route_id]:
                        if next_stop not in visited_stops:
                            queue.append((next_stop, num_bus + 1))
                            visited_stops.add(next_stop)

                    visited_routes.add(route_id)

        return -1
