from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        Input:
            A root of a binary tree, TreeNode
        Output:
            A list of list where each sublist refers to nodes in that respective tree level
        Assumptions:
            Children could have empty nodes -> point to None
            Children could have one side or more children nodes 
            I need to keep track of each level
                Once I encounter a new level, handle a list at that level
            I believe this is a Preorder traversal as I need to append the parent node then adjacent nodes, then children nodes from left to right
        
        Questions:
            How exactly do I keep track of each level?
                I could use some type of while loop, or for loop and once that loop exits I know at least one level has passed
                From there I could append a sublist to  my result list
            What data strucutre is the best for keeping track of what nodes still need to get processed
                Thinking a list maybe a deque

        high level approach:
            get root node, add it to the list
            hit new level, append new list to result
            hit first child node, add it to the result list
                add first left child to queue,
                add second right child to queue
            hit second child,
                rinse and repeat bada bing bada boom

        """
        
        if not root:
            return []

        res = []
        unresolved = deque()
        unresolved.append(root)

        while len(unresolved) > 0:
            res.append([])
            for i in range(len(unresolved)):
                node = unresolved.popleft()
                res[-1].append(node.val)
                if node.left:
                    unresolved.append(node.left)
                if node.right:
                    unresolved.append(node.right)
        

          
         
            
        return res