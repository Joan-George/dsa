"""
This class represents a solution for determining whether a given string of brackets is valid or not.
The class contains a single method, isValid, which takes a string as input and returns a boolean value indicating whether the string contains a valid arrangement of brackets.

Parameters:
- s (str): The input string containing brackets.

Returns:
- bool: True if the string contains a valid arrangement of brackets, False otherwise.

Example Usage:
    solution = Solution()
    result = solution.isValid("()[]{}")
    print(result)  # Output: True

    result = solution.isValid("([)]")
    print(result)  # Output: False
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        open_brackets = []
        open_characters = ["(", "[", "{"]

        for i in s:
            if i in open_characters:
                open_brackets.append(i)
            else:
                if not open_brackets:
                    return False
                last_character = open_brackets.pop()
                if i == ")" and last_character != "(":
                    return False
                elif i == "}" and last_character != "{":
                    return False
                elif i == "]" and last_character != "[":
                    return False

        if open_brackets:
            return False

        return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.isValid("()[]{}")
    print(result)  # Output: True
