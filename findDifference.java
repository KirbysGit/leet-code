class findDifference {
    // First Attempt....
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
}
