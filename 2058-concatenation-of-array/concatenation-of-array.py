class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = len(nums)
        ans = [0] * (2 * x)
        for i in range(x):
            ans[i] = nums[i]
            ans[i + x] = nums[i]
        return ans
