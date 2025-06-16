class Solution(object):
    def product_of_self_except_array(self, nums):
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            print(prefix, nums[i])
            result[i] = prefix
            prefix *= nums[i]
        print("result1:", result)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            print("psotfix:", postfix, "nums[i]:", nums[i], "result[i]:", result[i])
            result[i] *= postfix
            postfix *= nums[i]
        print(result)
        print([[]] * 3)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.product_of_self_except_array(nums=[1, 2, 3, 4]))
