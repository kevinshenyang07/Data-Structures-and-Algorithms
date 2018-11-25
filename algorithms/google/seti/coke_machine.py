# -*- coding: utf-8 -*-
import collections

# 可乐饮料机，有一系列按钮，每个按钮按下去会得到一定体积范围的可乐。先给定一个目标体积范围，问不限制按按钮次数，能否确定一定能得到目标范围内的可乐？
# 举例：有三个按钮，按下去得到的范围是[100, 120], [200, 240], [400, 410],
# 假设目标是[100, 110], 那答案是不能。因为按下一，可能得到120体积的可乐，不在目标范围里。
# 假设目标是[90, 120]，那答案是可以。因为按下一，一定可以得到此范围内的可乐。
# 假设目标是[300, 360], 那答案是可以，因为按下一再按二，一定可以得到此范围内
# 假设目标是[310, 360], 那答案是不能，因为按下一再按二，有可能得到300，永远没可能确定得到这个范围内的可乐。
# 假设目标是[1, 9999999999]，那答案是可以。随便按一个都确定满足此范围
class CokeMachine(object):

    # a better approach might be DP
    def can_fit(self, buttons, bottle):
        self.buttons = buttons
        self.min_lower, self.max_upper = bottle
        self.memo = collections.defaultdict(dict)
        return self.dfs(0, 0)

    def dfs(self, lower, upper):
        if upper in self.memo[lower]:
            return self.memo[lower][upper]
        if upper > self.max_upper:
            return False
        if lower >= self.min_lower and upper <= self.max_upper:
            return True

        for button in self.buttons:
            if self.dfs(lower + button[0], upper + button[1]):
                self.memo[lower][upper] = True
                return True

        self.memo[lower][upper] = False
        return False

if __name__ == '__main__':
    machine = CokeMachine()
    buttons = [[100, 120], [200, 240], [400, 410]]
    bottles = [[100, 110], [90, 120], [300, 360], [310, 360], [1, 9999]]
    #            false        true       true       false        true

    for bottle in bottles:
        print machine.can_fit(buttons, bottle)
