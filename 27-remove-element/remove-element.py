class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        while val in nums:
            nums.remove(val)
        """ 
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
        