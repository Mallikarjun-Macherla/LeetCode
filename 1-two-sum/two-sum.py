class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # BruteForce

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        temp = {}
        
        for i, num in enumerate(nums):
            res = target - num
            if res in temp:
                return [temp[res], i]
            temp[nums[i]] = i