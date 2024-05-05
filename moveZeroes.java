

// First Attempt.....
class moveZeroes{
    public void moveZeroesFirst(int[] nums) {
        if(nums.length == 1) return;
        int tmp = 0;


        int zeroPtr = 0; // both ptrs set to 0

        for (int idx = 0; idx < nums.length; idx++) {
            if (nums[idx] != 0) {
                tmp = nums[idx];
                nums[idx] = nums[zeroPtr];
                nums[zeroPtr] = tmp;
                zeroPtr++;
            }
        }
    }
}
