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
        for ts in self.logged.keys():
            if timestamp - ts >= 10:
                del self.logged[ts]
            elif message in self.logged[ts]:
                return False
        # do not add message to cache if already logged in last 10 sec
        self.logged[timestamp] = self.logged.get(timestamp, set())
        self.logged[timestamp].add(message)
        return True
