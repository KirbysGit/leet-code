// https://leetcode.com/problems/find-the-difference-of-two-arrays/
// 05 / 06 / 2024 - 9:13 pm
// sol - instead of sliding an entire window, just add / minus what is in "view"
// easy
// run-time -> 96.90%
// memory -> 98.38%


class findDifference {
    // First Attempt.... 05 / 06 / 2024 - 9:13 pm
    // Tried using only Arrays & List, lots of issues, then moved onto a HashMap to 
    // store the frequency of the values. Very slow approach, still trying to find faster.
    // RT - 9.34%, MEM - 89.47%
    public List<List<Integer>> findDifferenceFirst(int[] nums1, int[] nums2) {

        List<List<Integer>> myList = new ArrayList<>();

        List<Integer> innerList1 = new ArrayList<>();
        List<Integer> innerList2 = new ArrayList<>();

        HashMap<Integer,Integer> freq1 = new HashMap<Integer,Integer>();
        HashMap<Integer,Integer> freq2 = new HashMap<Integer,Integer>();

        for (int i = 0; i < nums1.length; i++) {
            if (freq1.containsKey(nums1[i])) {
                freq1.put(nums1[i], freq1.get(nums1[i]) + 1);
            } else {
                freq1.put(nums1[i], 1);
            }
        }

        for (int i = 0; i < nums2.length; i++) {
            if (freq2.containsKey(nums2[i])) {
                freq2.put(nums2[i], freq2.get(nums2[i]) + 1);
            } else {
                freq2.put(nums2[i], 1);
            }
        }

        for (int i = 0; i < nums2.length; i++) {
            if ((!(freq1.containsKey(nums2[i])))) {
                if (!(innerList2.contains(nums2[i]))) innerList2.add(nums2[i]);
            }
        }

        for (int i = 0; i < nums1.length; i++) {
            if ((!(freq2.containsKey(nums1[i])))) {
                if (!(innerList1.contains(nums1[i]))) innerList1.add(nums1[i]);
            }
        }

        myList.add(innerList1);
        myList.add(innerList2);

        return myList;

    }

    // Second Attempt... 05 / 06 / 2024 - 9:26 pm
    // Realized I was being stupid by using HashMap for Freq when HashSets do the job I was 
    // trying to do already. Swapped to Hashset then iterate through to check if exists in other set.
    // RT - 78.68%, MEM - 48.89%
    public List<List<Integer>> findDifferenceSecond(int[] nums1, int[] nums2) {

        List<List<Integer>> myList = new ArrayList<>();

        List<Integer> innerList1 = new ArrayList<>();
        List<Integer> innerList2 = new ArrayList<>();

        HashSet<Integer> freq1 = new HashSet<Integer>();
        HashSet<Integer> freq2 = new HashSet<Integer>();

        for (int i = 0; i < nums1.length; i++) {
            freq1.add(nums1[i]);
        }

        for (int i = 0; i < nums2.length; i++) { 
            freq2.add(nums2[i]);
        }

        for (int item : freq1) {
            if (!(freq2.contains(item))) {
                innerList1.add(item);
            }
        }

        for (int item : freq2) {
            if (!(freq1.contains(item))) {
                innerList2.add(item);
            }
        }
        

        myList.add(innerList1);
        myList.add(innerList2);

        return myList;

    }

    // Third Attempt... 05 / 06 / 2024 - 9:37 pm
    // Was looking at Solutions, almost all 100.00% solutions utilize some form of bitmasking for this problem.
    // However completing it without bitMasking I believe this is the best approach. Basically the only difference
    // is to remove from both Sets if contained in both instead of adding all the ones that are not in both.
    // RT - 96.90%, MEM - 98.38%
    public List<List<Integer>> findDifferenceBest(int[] nums1, int[] nums2) {

        List<List<Integer>> myList = new ArrayList<>();

        List<Integer> innerList1 = new ArrayList<>();
        List<Integer> innerList2 = new ArrayList<>();

        HashSet<Integer> freq1 = new HashSet<Integer>();
        HashSet<Integer> freq2 = new HashSet<Integer>();

        for (int i = 0; i < nums1.length; i++) {
            freq1.add(nums1[i]);
        }

        for (int i = 0; i < nums2.length; i++) { 
            freq2.add(nums2[i]);
        }

        for (int item : nums1) {
            if (freq2.contains(item)) {
                freq1.remove(item);
                freq2.remove(item);
            }
        }

        innerList1.addAll(freq1);
        innerList2.addAll(freq2);

        

        myList.add(innerList1);
        myList.add(innerList2);

        return myList;

    }
}
