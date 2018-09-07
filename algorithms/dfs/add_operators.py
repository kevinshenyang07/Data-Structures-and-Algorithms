# Expression Add Operators
# num only contains digits, can only add '+', '-' or '*' operator
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        self.num = num
        self.target = target
        self.exprs = []
        self.dfs('', 0, 0, 0)
        return self.exprs

    def dfs(self, path, pos, subtotal, multiple):
        # valid condition and stop condition
        if pos == len(self.num):
            if subtotal == self.target:
                self.exprs.append(path)
            return
        # use num[pos:i+1] as next number, then calculate new subtotal
        for i in range(pos, len(self.num)):
            if i > pos and self.num[pos] == '0':
                break
            curr_str = self.num[pos:i+1]
            curr = int(curr_str)
            if pos == 0:
                self.dfs(path + curr_str, i + 1, curr, curr)
            else:
                self.dfs(path + '+' + curr_str, i + 1, subtotal + curr, curr)
                self.dfs(path + '-' + curr_str, i + 1, subtotal - curr, -curr)
                self.dfs(path + '*' + curr_str, i + 1, subtotal - multiple + multiple * curr, multiple * curr)
                # 5 + 2 * 7 = (5 + 2) - 2 + 2 * 7
