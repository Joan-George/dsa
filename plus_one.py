"""
The Solution class provides a method called plusOne that takes a list of integers as input and returns a new list with the input list incremented by one.

Parameters:
- digits (List[int]): A list of integers representing the digits of a number.

Returns:
- List[int]: A new list of integers representing the digits of the input number incremented by one.

Example:
s = Solution()
result = s.plusOne([1, 2, 3])
print(result)
# Output: [1, 2, 4]

Note:
- The input list may contain leading zeros, which should be preserved in the output list.
- The input list may be empty, in which case an empty list should be returned.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        list_to_integer = int("".join([str(i) for i in digits]))
        integer_to_string = str(list_to_integer + 1)
        return [int(i) for i in list(integer_to_string)]

        # Convert the list of integers to a string
        digits_str = "".join(map(str, digits))

        # Increment the string representation of the number by one
        incremented_str = str(int(digits_str) + 1)

        # Convert the incremented string back to a list of integers
        incremented_digits = list(map(int, incremented_str))

        return incremented_digits


if __name__ == "__main__":
    s = Solution()
    result = s.plusOne([1, 2, 3])
    print(result)
