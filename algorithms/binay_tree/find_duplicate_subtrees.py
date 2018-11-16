# Find Duplicate Subtrees
# to compare any two subtrees, create an id for each subtree (called numbering method)
# => fingerprint of each subtree is (root.val, left_id, right_id)
# => in post order if a subtree has a new fingerprint, give it a new id
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        dup_nodes = {}  # id => nodes
        subtree_ids = {}  # (node, left_id, right_id) => id
        self.postorder(root, dup_nodes, subtree_ids)

        return [nodes[0] for nodes in dup_nodes.values() if len(nodes) > 1]


    # get id of the subtree
    def postorder(self, node, dup_nodes, subtree_ids):
        if not node: return 0

        left_id = self.postorder(node.left, dup_nodes, subtree_ids)
        right_id = self.postorder(node.right, dup_nodes, subtree_ids)

        fingerprint = (node.val, left_id, right_id)

        if fingerprint not in subtree_ids:
            subtree_ids[fingerprint] = len(subtree_ids) + 1

        root_id = subtree_ids[fingerprint]
        dup_nodes[root_id] = dup_nodes.get(root_id, [])
        dup_nodes[root_id].append(node)

        return root_id
# O(n) time and space
