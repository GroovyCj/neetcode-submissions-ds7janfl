# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right






class Solution:

    def search(self, root: Optional[TreeNode], res: list)  -> None:
        if not root:
            return
        
        self.search(root.left, res)
        res.append(root.val)
        self.search(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Input:
            The root of a binary tree -TreeNode
        Output:
            A List that represents the order of the binary tree,
                In order means it has to follow the order of the tree
        Assumptions:
            This tree is in ascending order, meaning both children nodes are bigger than the parent node
                The Right child is bigger than the left child
            A node can have a None value for its left and or right child
            This seems like a dfs tree we must get to the bottom of the current leg before we explore the parent node, and the other leg
        Questions:
        """


        res = []

        self.search(root=root, res=res)

        return res

        