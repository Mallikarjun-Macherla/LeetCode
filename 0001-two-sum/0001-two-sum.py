class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}  # val -> index
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in temp:
                return [temp[diff], i]
            temp[nums[i]] = i
