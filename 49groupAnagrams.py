# https://
# medium

class firstAttempt:

    # 01 / 20 / 2026 - 2:03 pm

    # Runtime -> 14 ms - 51.87%
    # Memory -> 22.12 MB - 33.34%
    
    # alright so with this i was really trying to just think through how to use
    # the counter as the key. but i was like oh wait i can't do that, and i can't do
    # a list.

    # so what i did was take each string, turn it to a list, sort it, then turn it back
    # to a string, then use that as the key in a dictionary and add the original string to
    # that value list.

    # then when i go through all the values per items in the dictionary all of the values
    # are grouped together.

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:
            tmp = list(word)
            tmp.sort()
            key = ("").join(tmp)
            seen.setdefault(key, []).append(word)

        out = []

        for (_, values) in seen.items():
            out.append(values)
        
        return out

class secondAttempt:

    # 01 / 20 / 2026 - 2:20 pm

    # Runtime -> 10 ms - 86.70%
    # Memory -> 22.81 MB - 12.52%

    # okay so we got around the tmp thing using tuple(sorted(str)).
    # as apparently you can use tuples as keys in a dict, and you can use sorted() on a str.

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:
            seen.setdefault(tuple(sorted(word)), []).append(word)

        out = []

        for (_, values) in seen.items():
            out.append(values)
        
        return out

class evenSimpler:

    # basically just instead of looping through with for loop, just use list(seen.values()).

    # same run time from what i saw though.

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:
            seen.setdefault(tuple(sorted(word)), []).append(word)

        return list(seen.values())
