from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        """
        Input:
            a nod ethat represents the starting point of a graph
                it contains a value
                and a list representing its neighbors
        Output:
            A list that is a deep copy of the graph as an adjancy list
                Each sublist represents the neighbors for that respective node
                
        Assumptions:
            I need to visit each node at least once to collect its neighbors
            from start to finish The return
        Questions: 
            How do I handle if a node doesn't have any neighbors?
            How do I handle if the input is empty?
        Approach ideas:
            I think for this problem I need to iterative go through each node collect its neighbors, 
            e.g. add them to a list, and append that list to the res once I fulfil adding all of the current neighbors
            I could then add those nodes to a queue to collect the neighors, and append them to a sublist
            I could have some type of datastructure so that I don't revist the same node twice or go into an infinite lop
        """

        if not node:
            return None
        
        # Map to store original node to its clone
        clones = {node: Node(node.val)}
        que: deque = deque([node])

        while que:
            curr = que.popleft()
            
            for n in curr.neighbors:
                if n not in clones:
                    # Create clone if it doesn't exist
                    clones[n] = Node(n.val)
                    que.append(n)
                # Link the clone of curr to the clone of neighbor n
                clones[curr].neighbors.append(clones[n])
            
        return clones[node]