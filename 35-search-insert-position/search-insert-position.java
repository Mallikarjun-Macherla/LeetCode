class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = 1;
        int n = nums.length - 1;
        int result = 0;

        if(nums[n] < target)
        {
            result = nums.length;
        } else
        {       

        while(right <= n)
        {
            if(nums[left] < target && nums[right] >= target)
            {
                result = right;
            }
                left++;
                right++;
            }
        }
        return result;
    }
}