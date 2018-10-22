# Logger Rate Limiter
# Design a logger system that receive stream of messages along with its timestamps,
# each message should be printed if and only if it is not printed in the last 10 seconds.
# The timestamp is in seconds granularity.
# It is possible that several messages arrive roughly at the same time.
# Example:
# Logger logger = new Logger();
# logger.shouldPrintMessage(1, "foo"); returns true;
# logger.shouldPrintMessage(2,"bar"); returns true;
# logger.shouldPrintMessage(3,"foo"); returns false;
# logger.shouldPrintMessage(8,"bar"); returns false;
# logger.shouldPrintMessage(10,"foo"); returns false;
# logger.shouldPrintMessage(11,"foo"); returns true;
# (not printed on ts=10, so on ts=11 the last ts "foo" is printed is 1)
class Logger(object):
    def __init__(self):
        self.logged = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        If this method returns false, the message will not be printed.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        # use .keys() to avoid deleting keys during dict iteration
        for ts in self.logged.keys():
            if timestamp - ts >= 10:
                self.logged.pop(ts)
            elif message in self.logged[ts]:
                return False
        # do not add message to cache if already logged in last 10 sec
        self.logged[timestamp] = self.logged.get(timestamp, set())
        self.logged[timestamp].add(message)
        return True


# Design Hit Counter
# Design a hit counter which counts the number of hits received in the past 5 minutes.
# Each function accepts a timestamp parameter (in seconds) and you may assume that calls are being made
# to the system in chronological order (ie, the timestamp is monotonically increasing).
# It is possible that several hits arrive roughly at the same time.
# Example:
# HitCounter counter = new HitCounter();
# counter.hit(1);
# counter.hit(2);
# counter.hit(3);
# counter.getHits(4); returns 3
# counter.hit(300);
# counter.getHits(300); returns 4
# counter.getHits(301); returns 3
# Approach: similar to problem above
# Followup: What if the number of hits per second could be very large? Does your design scale?
