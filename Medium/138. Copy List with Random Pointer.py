"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mapping = {}

        curr_node = head
        
        #needs 2 passes cause curr_node.next isnt mapped yet i think
        while curr_node:
            mapping[curr_node] = Node(curr_node.val)

            curr_node = curr_node.next

        curr_node = head
        while curr_node:
            mapping[curr_node].random = mapping.get(curr_node.random)
            mapping[curr_node].next = mapping.get(curr_node.next)

            curr_node = curr_node.next

        return mapping[head]
