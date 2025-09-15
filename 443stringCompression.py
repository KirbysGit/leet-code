# https://leetcode.com/problems/string-compression/
# medium

class firstAttempt:

    # again i had to use chatgpt towards the end, was able to get 70/77 but i just
    # kept going back and forth on the logic, and i felt i wasn't really understanding
    # but just trying a bunch of different ideas

    # 09 / 10 / 2025 - 4:01pm

    # Runtime -> 0ms - 100.00%
    # Memory -> 17.93 MB - 14.22%

    # alright so idea i had was basically this but i just couldn't get around the logic
    
    # but this process works with two pointers, one at the current char, and one
    # that increments until the char is different

    # j will iterate until the char is different, then once we get that
    # we can get the count of the char, and if it's greater than 1, we can delete
    # the chars between i and j, and then add the count to the list
    # then we can increment i by 1 + the length of the digits

    # if the count is 1, we just increment i by 1 as we don't add anything

    # then we return the length of the list

    # i was misunderstanding the indexing honestly, like i couldn't wrap my head around
    # the chars[i+1:j]

    def compress(self, chars: List[str]) -> int:
        i = 0

        while i < len(chars):
            j = i + 1
            while (j < len(chars)) and (chars[i] == chars[j]):
                j+=1

            count = j - i

            if (count > 1):
                del chars[i+1:j]
                digits = list(str(count))
                chars[i+1:i+1] = digits
                i+= 1 + len(digits)
            else:
                i+=1
        
        return len(chars)