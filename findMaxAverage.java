//https://leetcode.com/problems/maximum-average-subarray-i/
// 05 / 05 / 2024 - 4:47 am
// sol - instead of sliding an entire window, just add / minus what is in "view"
// easy
// run-time -> 63,97%
// memory -> 48.30%

class findMaxAverage {
    // First Attempt.... 
    // Summing All Windows, skipping if Next Val in Smaller then Last Val out
    // RT - 5.00%, MEM - 20.98%
    public double findMaxAverageFirst(int[] nums, int k) { 
        if (nums.length == 1) return nums[0];
        double bestSum = Integer.MIN_VALUE;
        double curSum = 0;
        for (int i = 0; i <= nums.length - k; i++) {
            curSum = 0;
            if ((i > 0) && (i <= nums.length - k) && (nums[i + k - 1] < nums[i - 1])) continue;
            for (int j = i; j < k + i; j++) {
                curSum += nums[j];
            }
            bestSum = Math.max(curSum, bestSum);
        }
        return bestSum / k;
    }

    // Second Attempt....... 
    // Summing first window, then incrementing / decrementing based on last out first in values.
    // RT - 41.47%, MEM - 73.38%
    public double findMaxAverageSecond(int[] nums, int k) {
        if (nums.length == 1) return nums[0];
        double curSum = 0;

        for (int j = 0; j < k; j++) curSum += nums[j];

        double bestSum = curSum;

        for (int i = 1; i <= nums.length - k; i++) {
            curSum = curSum - nums[i - 1] + nums[k + i - 1];
            bestSum = Math.max(curSum, bestSum);
        }

        return bestSum / k;
    }

    // Third Attempt...
    // All I changed from 2nd Attempt was preventing the checker func from being called when not needed.
    // Somehow got slower tho. 
    // RT - 16.51%, MEME - 78.44%
    public double findMaxAverageThird(int[] nums, int k) {
        if (nums.length == 1) return nums[0];
        double curSum = 0;

        for (int j = 0; j < k; j++) {
            curSum += nums[j];
        }

        double bestSum = curSum;

        for (int i = 1; i <= nums.length - k; i++) {
            curSum = curSum - nums[i - 1] + nums[k + i - 1];
            if (nums[i - 1] < nums[k + i - 1]) bestSum = Math.max(curSum, bestSum);
        }

        return bestSum / k;
    }

    // Best One....
    // Found in LeetCode Solutions tab for this problem.
    // I think Java is just slower for this type of problem as it this is the fastest that I could find.
    // RT - 63.97%, MEM - 48.30%
    public double findMaxAverageBest(int[] nums, int k) {
        double ans = 0;
        double window = 0;

        // Calculate the first window
        for(int i = 0; i < k; i++) {
            window = window + nums[i];
        }

        // The window variable is the sum of all the numbers
        // We need to divide window for k to find the average
        ans = window / k;

        // Move the window to the right
        for(int right = k; right < nums.length; right++) {
            window += nums[right] - nums[right - k]; // Add right-one and delete left-one
            ans = Math.max(ans, window / k); // Check the higher average on every slide of the window
        }

        return ans;
    }
  
}
