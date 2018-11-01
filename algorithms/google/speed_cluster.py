# speed cluster
# Imagine a scenario where there are N cars on an infinitely long single-lane road.
# Each car has a unique, permanent integer speed ranging between 1 and N, inclusive (units are irrelevant).
# The cars can be placed in any order along the road and then told to start driving indefinitely.
# Let's assume that the cars are traveling from right-to-left. So the leftmost car is at the front.
# Given an ordering of N cars, construct an algorithm to return an array of cluster sizes.
# f([2, 4, 1, 3]) => [2, 2]
# f([2, 5, 4, 3, 1]) => [4, 1]  (5, 4, 3 can catch 2)
class Solution(object):
    def get_cluster_sizes(self, speeds):
        cluster = []
        sizes = []

        for speed in speeds:
            if not cluster or cluster[0] <= speed:
                cluster.append(speed)
            else:
                sizes.append(len(cluster))
                cluster = [speed]

        if cluster:
            sizes.append(len(cluster))

        return sizes

    def test(self):
        print self.get_cluster_sizes([2,4,1,3])
        print self.get_cluster_sizes([2,5,4,3,1])

if __name__ == '__main__':
    Solution().test()

# followup: if a car with speed N + 1 is added to sppeds, how would the output changes?
# 加在任何位置就只会影响那个位置的cluster的len，从len变成len+1。corner case就是加在第一个位置，会出来一个1为长度的cluster
