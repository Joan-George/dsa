class Solution(object):
    def contains_duplicate(self, nums=[]):

        hashset = set()

        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()
    result = solution.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print(result)
