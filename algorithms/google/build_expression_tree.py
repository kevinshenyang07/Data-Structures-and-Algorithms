import collections

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Parser(object):
    # operator stack + output stack
    def build_expression_tree(self, expr):
        if not expr: return None
        # both stacks have tree node as element
        output = []
        operators = []
        curr_num = 0

        for i, char in enumerate(expr):
            if char in '+-*/':
                operators.append(TreeNode(char))
            else:
                curr_num = 10 * curr_num + int(char)

                if i == len(expr) - 1 or not expr[i + 1].isdigit():
                    output.append(TreeNode(curr_num))
                    # when the last operator has higher precedence
                    if operators and operators[-1].val in '*/':
                        self.build(output, operators)
                    curr_num = 0
        # build tree
        root = None
        while operators:
            root = self.build(output, operators)
        return root

    def build(self, output, operators):
        root = operators.pop()
        root.right = output.pop()
        root.left = output.pop()
        output.append(root)
        return root

    def preorder(self, root):
        if not root: return
        print root.val
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == '__main__':
    parser = Parser()
    root = parser.build_expression_tree('11+2*30-4')
    parser.preorder(root)
