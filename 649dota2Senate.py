# https://leetcode.com/problems/dota2-senate/
# medium

class firstAttempt:

    # 09 / 26 / 2025 - 1:27 am

    # Runtime -> 4062 ms - 5.00% - WOOHOOO!!!! 5%!!!!!
    # Memory -> 17.72 MB - 98.12%

    # alright this shit is incredibly slow, i had to use chatGPT, i spent like 2 hours
    # trying to figure it out, but i just don't understand how queue work well enough.

    # coming back to this tmrw, need to go to sleep, but gonna optimize it because this blows.

    # idea is while there is two parties, pop index.
    # check if radiant, 
    #   if so, check if our ban is greater than 0, if so, vote means nothing, just decrement ban
    # check if dire,
    #   if so, check if our ban is greater than 0, if so, vote means nothing, just decrement ban
    # after all when votes are only one party, return that party.
    def predictPartyVictory(self, senate: str) -> str:

        votes = list(senate)

        banR = 0
        banD = 0

        while len(set(votes)) == 2:
            vote = votes.pop(0)
            if vote == 'R':
                if banR > 0:
                    banR-=1
                else:
                    votes.append('R')
                    banD+=1
            else:
                if banD > 0:
                    banD-=1
                else:
                    votes.append('D')
                    banR+=1
        
        if set(votes) == {'R'}:
            return 'Radiant'
        else:
            return 'Dire'