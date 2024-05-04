"""
This class represents a solution for finding the longest common prefix among a list of strings.

Methods:
- longestCommonPrefix(strs): Finds the longest common prefix among the given list of strings.

Attributes:
- None

Example Usage:
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(strs)
    print(result)  # Output: "fl"
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = ""
        for i in range(len(strs[0])):
            prefix = strs[0][: i + 1]
            for j in strs:
                try:
                    if prefix == j[: i + 1]:
                        continue
                    else:
                        return prefix[: len(prefix) - 1]
                except:
                    return prefix[: len(prefix) - 1]

        return prefix


if __name__ == "__main__":
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(strs)
    print(result)  # Output: "fl
