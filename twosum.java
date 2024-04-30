// https://leetcode.com/problems/two-sum/
// 4 / 30 / 2024 - 2:12 am
// sol - hashmap to hold values for access during its and prevent o(n^2) run time

// hashmap api -> containsKey, get
// arr api -> length

class twosum {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer,Integer> seen = new HashMap<>(); // declare hashmap idx to val
        int [] ans = new int [2]; // declare ans arr

        for (int i = 0; i < nums.length; i++) { // for val in nums arr

            if (seen.containsKey(target - nums[i])) { // if diff already contained in map

                ans[0] = seen.get(target - nums[i]); // first idx = hash idx
                ans[1] = i; // second idx = cur idx
                return ans; // return arr

            }

            seen.put(nums[i], i); // else add val & idx to map
        }

        return null; // if nothing (impossible) return null
    }
}
