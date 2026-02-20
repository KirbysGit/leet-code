# https://leetcode.com/problems/reverse-nodes-in-k-group/
# hard

class planningOut:

    # 02 / 20 / 2026 - 3:38 pm

    # the way i'm looking at it right now is like we do the copy approach while iterating
    # through list. 

    # so like what we did in the last problem #92. where we copy the nodes assuming
    # the indexes are like in the pairing of 2's. then if its the case that is less than
    # k amount, then we just don't change it. 

    # but basically like loop through, doing like while (k) then resetting at every 
    # k amount. then basically change the nodes to the new copied group. 