# https://leetcode.com/problems/search-suggestions-system/
# medium

class firstAttempt:

    # 11 / 11 / 2025 - 10:27 pm

    # Runtime -> 4 ms - 91.60%
    # Memory -> 20.50 MB - 75.07%

    # i literarlly put zero thought into this problem outside of asking chatgpt if what
    # i was trying to do was right. and funny enough, IT WASN'T!!!! 

    # basically i was like okay can we just use the same data structure from yesterday's
    # problem, but like we would have to set it up which could be a long operation as its
    # per char per word. but we tried it and chatgpt said it was right!

    # so i worked with taht for a bit, then i was like okay, how can we get three options
    # from our search query that we had previously set up. and it was like use a dfs! so
    # trying to set that up was a pain, and i had to use chatgpt to help me do that. insane
    # i know. but then eventually it gets set up, and its like working for our sample
    # cases but then when we submit it, it just gives wrong answers, and tbh i still
    # don't really know why! it looked like it had the right set up, it just broke 
    # for some of the long test cases, probably becasue of the dfs. 

    # but then chatgpt recommended the binary search approahc, which looks way simpler
    # and it works which is pretty big i guess.

    # i'll place the solution below, and explain it from my udnerstanding rq.

    # basically sort the products, (my initial thought too)
    
    # then we initialize some vars to hold our results and the prefix.

    # then we iterate for ch in searchWord, add that char to our prefix.
    # then we use bisect_left with our prefix to find the first index where the prefix
    # could be inserted. then we set suggestions to an empty list, and we iterate through
    # the next 3 lexicographically sorted products, and if it starts with our prefix,
    # we append it to our suggestions list, then we add that list to our results.
    

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            # Find first index where prefix could be inserted
            i = bisect.bisect_left(products, prefix)
            suggestions = []
            # Check next 3 lexicographically sorted products
            for w in products[i:i+3]:
                if w.startswith(prefix):
                    suggestions.append(w)
            res.append(suggestions)
        return res