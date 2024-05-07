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


    // Second Attempt... 05 / 06 / 2024 - 10:17 pm
    // Use of .values() in the HashMap API, Didn't know about that.
    // Gets rid of 2nd HashSet, and saves multiple lines of code.
    // RT - 96.73%, MEM - 92.94%
    public boolean uniqueOccurrencesSecond(int[] arr) {
        
        HashMap<Integer,Integer> freq = new HashMap<Integer,Integer>();
        HashSet<Integer> values = new HashSet<Integer>();

        for (int i = 0; i < arr.length; i++) {
            if (freq.containsKey(arr[i])) {
                freq.put(arr[i], freq.get(arr[i]) + 1);
            } else {
                freq.put(arr[i], 1);
            }
        }

        for (int item : freq.values()) {
            if (values.contains(item)) {
                return false;
            } else {
                values.add(item);
            }
        }

        return true;
    }
}
