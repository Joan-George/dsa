"""
The Solution class represents a solution for converting a Roman numeral string to an integer value.

Methods:
- romanToInt(s): Converts the given Roman numeral string to an integer value.

Attributes:
- None

Example usage:
    solution = Solution()
    result = solution.romanToInt("III")
    print(result)  # Output: 3
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        roman_numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}


        while i < len(s):
            current_character = s[i]
            current_value = roman_numerals[current_character]

            if i < len(s) - 1:
                next_character = s[i + 1]
                next_value = roman_numerals[next_character]

                if current_value < next_value:
                    num += (next_value - current_value)
                    i += 2  # Move to the character after the next character
                else:
                    num += current_value
                    i += 1
            else:
                num += current_value
                i += 1

        return num

if __name__ == "__main__":
    s = Solution()
    roman="MCMXCIV"
    print(s.romanToInt(roman))