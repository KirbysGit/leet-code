//https://leetcode.com/problems/greatest-common-divisor-of-strings/
// 05 / 03 / 2024 - 1:41 am
// sol - gcd of with strings
// easy
// run-time -> 100.00%
// memory -> 89.78%


class  gcdOfStrings {
        
        // First Attempt...
        public String gcdOfStringsFirst(String str1, String str2) {
                StringBuilder res = new StringBuilder();
                StringBuilder tmp = new StringBuilder();
                int min = Math.min(str1.length(), str2.length());

                for (int i = 0; i < min; i++) {
                        if(str1.charAt(i) != str2.charAt(i)) break;
                        res.append(str1.charAt(i));
                        if (str2.contains(res) && str1.contains(res)) tmp = res;
                }

                if (!(res.isEmpty())) {
                    while (((str1.length() % tmp.length()) != 0) || ((str2.length() % tmp.length()) != 0)) {
                        tmp.deleteCharAt(tmp.length() - 1);
                    }
                    System.out.println(tmp.toString());
            
                    int max = Math.max(str1.length(), str2.length());
                    
                    StringBuilder another = new StringBuilder();
        
                    for (int i = 0; i < (max / tmp.length()); i++) {
                        another.append(tmp);
                        if (another.length() == str1.length()) {
                            System.out.println("In here");
                            if (((another.toString()).compareTo(str1)) != 0) return ""; 
                        }
                        if (another.length() == str2.length()) {
                            if (((another.toString()).compareTo(str2)) != 0) return "";
                        }
                    }
        
                    while (((str1.length() % tmp.length()) != 0) || ((str2.length() % tmp.length()) != 0)) {
                        tmp.deleteCharAt(tmp.length() - 1);
                    }
                }
                return tmp.toString();
        }

        // Optimized....
        public String gcdOfStringsOptimized(String str1, String str2) {
        
                if (!(str1 + str2).equals(str2 + str1)) return "";

                int gcd = gcd (str1.length(), str2.length());

                return str1.substring(0, gcd);

            }

        private int gcd (int a, int b) {
                return b == 0 ? a : gcd(b, a % b);
            }

}

