"""Given an integer array nums, find the subarray (A subarray is a contiguous non-empty sequence of elements within an array)
with the largest sum, and return its sum."""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
            print(cur_sum, max_sum)

        return max_sum


if __name__ == "__main__":
    s = Solution()
    result = s.maxSubArray([2, 5, 2, -5, -2, 3, -7, 2, 6, 1, 1, 2])
    print(result)
