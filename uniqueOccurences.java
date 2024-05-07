// https://leetcode.com/problems/unique-number-of-occurrences/
// 05 / 06 / 2024 - 10:00 pm
// sol - 
// easy
// run-time -> **
// memory -> **

class uniqueOccurences {

    // First Attempt... 05 / 06 / 2024 - 10:00 pm
    // Utilizing HashMap to store frequency of items, and hashset to store individual items.
    // Then add each frequency of value to another Hashset checking if it is contained per addition, if so, break.
    // RT - 32.63%, MEM - 30.57%
    public boolean uniqueOccurrencesFirst(int[] arr) {
        
        HashMap<Integer,Integer> freq = new HashMap<Integer,Integer>();
        HashSet<Integer> values = new HashSet<Integer>();
        HashSet<Integer> numValues = new HashSet<Integer>();

        for (int i = 0; i < arr.length; i++) {
            values.add(arr[i]);
            if (freq.containsKey(arr[i])) {
                freq.put(arr[i], freq.get(arr[i]) + 1);
            } else {
                freq.put(arr[i], 1);
            }
        }

        for (int item : values) {
            if (numValues.contains(freq.get(item))) {
                return false;
            } else {
                numValues.add(freq.get(item));
            }
        }

        return true;

        
    }
}
