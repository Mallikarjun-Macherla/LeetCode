class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        x = 0
        for i in range(1, len(nums)):
            if nums[i] != nums [x]:
                x += 1
                nums[x] = nums[i]
        return x + 1