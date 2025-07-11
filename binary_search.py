from typing import List


class Solution(object):

    def binarySearch(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.binarySearch([1, 2, 4, 5, 6, 7, 8], 6))
