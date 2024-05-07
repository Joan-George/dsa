# Definition for singly-linked list.

"""
Class representing a node in a singly-linked list.

Attributes:
    val (int): The value stored in the node.
    next (ListNode): The reference to the next node in the list.

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
The Solution class provides a method mergeTwoLists that takes in two optional ListNode objects, list1 and list2, and returns an optional ListNode object.

Parameters:
- list1 (Optional[ListNode]): The first ListNode object to be merged.
- list2 (Optional[ListNode]): The second ListNode object to be merged.

Returns:
- Optional[ListNode]: The merged ListNode object.

The mergeTwoLists method merges the two input ListNode objects in ascending order and returns the merged ListNode object.
It creates a new ListNode object called head as the starting point of the merged list.
It then iterates through the two input lists, comparing the values of the current nodes and appending the smaller value to the result list.
The iteration continues until one of the input lists is exhausted.
Finally, it appends the remaining nodes from the non-exhausted list to the result list.

Example usage:
solution = Solution()
result = solution.mergeTwoLists(list1, list2)
"""


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        result = head
        print(head)
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next

        if list1:
            result.next = list1
        elif list2:
            result.next = list2

        return head.next


l1 = ListNode()
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode()
l2.next = ListNode(1)
l2.next.next = ListNode(3)
l2.next.next = ListNode(4)

result = Solution().mergeTwoLists(l1, l2)
print(l1)
