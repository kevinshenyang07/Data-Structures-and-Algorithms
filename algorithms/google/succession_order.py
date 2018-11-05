# 王位继承，长子及其后代有优先级继承权，其次是次子及其后代，以此类推。完成以下几个API:
# - void birth(String parent, String name) // 父亲名字和孩子名字，生个娃
# - void death(String name) // 此人要死
# - List<String> getOrderOfSuccession() // 返回当前的继承顺序，死人不能出现
# 三个function会被反复调用，实现function细节
class Person(object):
    def __init__(self, name):
        self.name = name
        self.dead = False
        self.children = []

class SuccessionOrder(object):
    def __init__(self):
        self.family = {}
        self.root = None

    def birth(self, parent_name, child_name):
        # validation
        child = Person(child_name)
        if not self.root:
            self.root = child
        else:
            parent = self.family[parent_name]
            child = Person(child_name)
            parent.children.append(child)
        self.family[child_name] = child

    def death(self, name):
        # validation
        self.family[name].dead = True

    def get_order_of_succession(self):
        order = []
        self.dfs(self.root, [])
        return oreder

    def dfs(self, person, order):
        if not person:
            return
        if not person.dead:
            order.append(person)
        for child in person.children:
            self.dfs(child, order)
# followup: how to optimize space complexity
