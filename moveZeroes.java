//

// First Attempt.....
class moveZeroes {
    public void moveZeroesFirst(int[] nums) { // RT - 85.96%, MEM - 86.25% // I think this is best solution for Java?

        int zeroPtr = 0; 

        for (int idx = 0; idx < nums.length; idx++) {
            if (nums[idx] != 0) {
                int tmp = nums[idx];
                nums[idx] = nums[zeroPtr];
                nums[zeroPtr] = tmp;
                zeroPtr++;
            }
        }
    }
}
