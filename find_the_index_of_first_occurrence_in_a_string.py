"""
The Solution class provides a method strStr() that finds the first occurrence of a substring (needle) within a string (haystack).

Parameters:
    - haystack (str): The string to search within.
    - needle (str): The substring to search for.

Returns:
    - int: The index of the first occurrence of the substring within the string. If the substring is not found, -1 is returned.

Example Usage:
    s = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    result = s.strStr(haystack=haystack, needle=needle)
    print(result)  # Output: 0

Note:
    - The method uses a sliding window approach to check if the substring matches a portion of the string.
    - If the substring is found, the method returns the index of the first character of the substring within the string.
    - If the substring is not found, -1 is returned.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        Find the index of the first occurrence of a substring in a given string.

        :param haystack: The string to search in.
        :type haystack: str
        :param needle: The substring to search for.
        :type needle: str
        :return: The index of the first occurrence of the substring in the string, or -1 if the substring is not found.
        :rtype: int
        """

        # if(needle in haystack):
        #     return haystack.index(needle)

        first_char = needle[0]

        for i in range(len(haystack)):
            if haystack[i] == first_char and haystack[i : i + len(needle)] == needle:
                return i

        return -1


if __name__ == "__main__":
    s = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    result = s.strStr(haystack=haystack, needle=needle)
    print(result)
