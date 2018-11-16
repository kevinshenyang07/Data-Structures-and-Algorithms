# Fruit Into Baskets
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        num_fruits = 0
        counter = {}
        i = 0

        for j, fruit in enumerate(tree):
            # include tree[j] in the window anyway
            counter[fruit] = counter.get(fruit, 0) + 1

            if len(counter) <= 2:
                # tree[j] counts
                num_fruits = max(num_fruits, j - i + 1)
            else:
                # tree[j] does not count
                num_fruits = max(num_fruits, j - i)
                # shrink the window from the left until it's valid
                while len(counter) > 2:
                    last_fruit = tree[i]
                    counter[last_fruit] -= 1
                    if counter[last_fruit] == 0:
                        counter.pop(last_fruit)
                    i += 1

        return num_fruits
# test cases:
# [1,2,3,2,2] => 4
# [1,0,1,4,1,4,1,2,3] => 5
# [3,3,3,1,2,1,1,2,3,3,4] =? 5
