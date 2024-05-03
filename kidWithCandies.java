//https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
// 05 / 03 / 2024 - 3:02 pm
// sol - find max, add max to all values, check.
// easy
// run-time -> 84.98%
// memory -> 66.24%

// First Attempt...
class kidWithCandies {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for (int i = 0; i < candies.length; i++) {
            if (max < candies[i]) {
                max = candies[i];
            }
        }

        List<Boolean> myList = new ArrayList<Boolean>(candies.length);

        for (int i = 0; i < candies.length; i++) {
            if ((candies[i] + extraCandies) >= max) {
                myList.add(true); 
            } else {
                myList.add(false);
            }
        }

        return myList;
    }
}



