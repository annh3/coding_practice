# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Can you basically use DFS?

Yes, let's practice

DFS for cycle detection used a in_process set and visited set
We only add a node to visited after we are done processing it

Does this work as-is if we want to find the beginning of the cycle?
Yes, the first backedge points to the beginning
"""

class Solution:
    def DFS(self, cur, in_process):
        if cur == None:
            return None
        in_process.add(cur)
        if cur.next in in_process:
            return cur.next
        else:
            return self.DFS(cur.next, in_process)
        in_process.remove(cur)
        
    def detectCycle(self, head: ListNode) -> ListNode:
        in_process = set()
        node = self.DFS(head, in_process)
        #print("tail connects to node index "+str(pos))
        return node
