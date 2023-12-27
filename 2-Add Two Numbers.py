# Time complexity: O(n + m)
# Space complexity: O(max(n, m))

# n: Length of the first linked list (l1)
# m: Length of the second linked list (l2)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # Turn linked list to integer
    def getInt(self,nl) -> int:
        result = 0
        power = 0
        while nl != None:
            result += (nl.val) * pow(10,power)
            power += 1
            nl = nl.next
        return result

    # Turn integer to linked list
    def getList(self,result) -> ListNode:
        ans = None
        for i in str(result): 
            ans = ListNode(int(i),ans)
        return ans

    def addTwoNumbers(self, l1, l2):
        return self.getList(self.getInt(l1) + self.getInt(l2))