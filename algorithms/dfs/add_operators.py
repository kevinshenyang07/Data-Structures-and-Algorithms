# Expression Add Operators
# num only contains digits, can only add '+', '-' or '*' operator
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(path, pos, subtotal, multiple):
            # valid condition and stop condition
            if pos == len(num):
                if subtotal == target:
                    exprs.append(path)
                return
            # use num[pos:i+1] as next number, then calculate new subtotal
            for i in range(pos, len(num)):
                if i > pos and num[pos] == '0':
                    break
                curr_str = num[pos:i+1]
                curr = int(curr_str)
                if pos == 0:
                    dfs(path + curr_str, i + 1, curr, curr)
                else:
                    dfs(path + '+' + curr_str, i + 1, subtotal + curr, curr)
                    dfs(path + '-' + curr_str, i + 1, subtotal - curr, -curr)
                    dfs(path + '*' + curr_str, i + 1, subtotal - multiple + multiple * curr, multiple * curr)
                    # 5 + 2 * 7 = (5 + 2) - 2 + 2 * 7

        if not num:
            return []

        exprs = []
        dfs('', 0, 0, 0)
        return exprs
