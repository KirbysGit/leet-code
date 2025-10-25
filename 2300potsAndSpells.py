# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# medium

class firstAttempt:

    # this did not work!

    # i felt i have hte right approach but its too slow, probably because its borderline o(n^2)
    # so i'm gonna work for a diff approach.

    def wizardShit(self, s, pots, success):
        if not pots:
            return None

        need = math.ceil(success / s)
        n = len(pots)
        for pot in pots:
            if pot >= need:
                break
            n-=1
        
        return n


    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()

        pairs = []

        for spell in spells:
            pairs.append(self.wizardShit(spell, potions, success))

        return pairs

    # alright i don't feel like making another class for the next attempt, but chatpgt changed
    # two lines on my thing. no idea what bisect is but it seems like a binary search thing
    # to get the value we need, so what i was doing, but instead doing it with a binary search
    # instead of a for loop.

    # Runtime -> 197 ms - 62.31%
    # Memory -> 42.66 MB - 54.32%

    def wizardShit(self, s, pots, success):
        if not pots:
            return None

        need = math.ceil(success / s)
        n = len(pots)
        idx = bisect.bisect_left(pots, need)
        return len(pots) - idx

class fasterSolution:

    # same sort of approach, just didn't use the separate function, and honestly looking at
    # it i don't know why i thought i needed it. i think its because i was using the
    # separate loop in that too, so i didn't want it to be o(n^2) even tho moving it 
    # to another function wouldn't change that. IM SO FUCKING STUPID. nah not actaully,
    # had good intent.

    # Runtime -> 139 ms - 91.47%
    # Memory -> 42.92 MB - 17.97%

    # but the secret is in that bisect_left function. 
    
    # its a binary search function that finds the exact index where the element should go
    # to keep the list sorted. and also since the lists are 0 indexed, we don't need to
    # deal with a -1 sort of set up, instead we can just subtract that index from the length to
    # get all of the pots that are "above" the target. then we add 

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        m = len(potions)
        for i in spells:
            target = ceil(success / i)
            idx = bisect.bisect_left(potions, target)
            result.append(m - idx)
        return result


    