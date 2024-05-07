// https://leetcode.com/problems/removing-stars-from-a-string/
// 05 / 06 / 2024 - 10:38 pm
// sol - 
// medium
// run-time -> *
// memory -> *

class removeStars {

    // First Attempt... 05 / 06 / 2024 - 10:38 pm
    // Change Str to Char Arr, then create stack, iterating through Char Arr
    // If Star Pop Last Char, Else Add Char.
    // Then Using StringBuilder, add each element popped off stack to String.
    // Then Reverse because Pop is Backwards. And Return.
    // RT - 58.40%, MEM - 25.22%
    public String removeStarsFirst(String s) {
        
        char [] list = s.toCharArray();
        Stack<Character> myStack = new Stack<Character>();
        int stars = 0;

        for (int i = 0; i < list.length; i++) {
            if (list[i] != '*') {
                myStack.push(list[i]);
            } else {
                stars++;
                char tmp = myStack.pop();
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < (list.length - (stars * 2)); i++) {
            sb.append(myStack.pop());
        }

        sb.reverse();

        return sb.toString();
    }
}
