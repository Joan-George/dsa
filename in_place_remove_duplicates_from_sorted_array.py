"""
This class provides a solution for removing duplicates from a given list of integers.

Methods:
    removeDuplicates(nums): Removes duplicates from the given list and returns the length of the modified list.

Attributes:
    None
"""


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
    Removes duplicate elements from a given list of integers.

    Parameters:
        nums (List[int]): The list of integers from which duplicate elements need to be removed.

    Returns:
        int: The length of the modified list after removing duplicate elements.

    Example:
        s = Solution()
        arr = [1, 1, 2, 2, 2, 3, 3]
        k = s.removeDuplicates(arr)
        # k = 3
        # arr = [1, 2, 3]

    """

        j = 0
        print(nums)
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1


if __name__ == "__main__":
    s = Solution()
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = s.removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
