# https://leetcode.com/problems/isomorphic-strings/
# easy

class firstAttempt:

    # 1 / 17 / 2026 - 9:42 pm

    # 42 / 47 test cases passed.

    # in my mind i was like okay, the main thing we need to consider is if 
    # the values of each letter come out to the same. like if its "bbbb" and "aaaa"
    # if they're equal then they're isomorphic.

    # i did this through two counters between the strings, then sorting them in 
    # descending order, then comparing the values as we iterate through returning
    # false if there is any that isn't the same.

    # i found out this didn't work because it didn't consider the order of the letters.

    def isIsomorphic(self, s: str, t: str) -> bool:
        
        sCount = Counter(s)
        tCount = Counter(t)
        
        sorted(sCount.items(), key=lambda x: x[1])
        sorted(tCount.items(), key=lambda x: x[1])

        for (k1, v1), (k2, v2) in zip(sCount.items(), tCount.items()):
            if v1 != v2:
                return False
        
        return True

class secondAttempt:

    # 1 / 17 / 2026 - 10:12 pm

    # alright i know it sounds bs.

    # but im super tired right now and i was trying to wrap my head
    # around this problem. i wanted to do a 2d sort of connection just checking
    # if its in it, or if not then just add it both ways.

    # my brain wasn't helping me out. 

    # consulted the gpt from this attempt below on how i could do it 
    # in a 2D way. thats how i got to the next solution.

    def isIsomorphic(self, s: str, t: str) -> bool:
        
        connect = {}

        for idx in range(len(s)):
            if connect.get(s[idx], '.') == '.':
                connect[s[idx]] = t[idx]
            else:
                if connect[s[idx]] != t[idx]:
                    return False
        
        return True

class correctSolution:

    # 1 / 17 / 2026 - 10:13 pm

    # this one basically just does what i did in the last one
    # gets rid of the default check with the '.' and just checks
    # membership, and then adds it both ways across two dicts.

    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        for idx in range(len(s)):
            ct = t[idx]
            cs = s[idx]

            if cs in s_to_t and s_to_t[cs] != ct:
                return False
            if ct in t_to_s and t_to_s[ct] != cs:
                return False

            s_to_t[cs] = ct
            t_to_s[ct] = cs

        return True