

import java.util.*;

/*
First Attempt....
class Solution { 
    public String mergeAlternately(String word1, String word2) {

        if (word1.isEmpty()) return word2;
        if (word2.isEmpty()) return word1;

        char [] char1 = word1.toCharArray();
        char [] char2 = word2.toCharArray();

        int len = word1.length() + word2.length() + 1;

        char [] res = new char [len - 1];
        int max = Math.max(word1.length(), word2.length());
        int ptr1 = 0;
        int ptr2 = 0;
        int idx = 0;
        while (true) {
            if ((ptr2 >= max) || (ptr1 >= max)) break;
            if (ptr1 < char1.length) {
                res[idx] = char1[ptr1];
                ptr1++;
                idx++;
            }
            if (ptr2 < char2.length) {
               res[idx] = char2[ptr2];
               ptr2++;
               idx++;
            }
            System.out.println(res);
        }


        return String.join("", String.valueOf(res));
    }
}
*/

// Optimized...
class mergeAlternatively {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder();
        int idx = 0;

        while (idx < word1.length() || idx < word2.length()) {
            if (idx < word1.length()) {
                res.append(word1.charAt(idx));
            }
            if (idx < word2.length()) {
                res.append(word2.charAt(idx));
            }
            idx++;
        }
        return res.toString();
    }
}

