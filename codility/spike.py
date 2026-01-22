# from an interview OA i did.

# basically i was given an list of integers, we needed to create the longest possible
# spike across the array. look at the examples i remember below :

# input -> [1, 2, 3, 2, 3, 2, 2] 
# output -> 4
# reasoning -> ordering spike like [1, 2, 2, 3, 2, 2] -> [1, 2, 3, 2] -> 4

# basically if the values are the same the spike isn't increasing in length.

# input -> [1, 2]
# output -> 2
# reasoning -> already ordered like a spike.

# input -> [2, 2, 2]
# output -> 1
# reasoning -> only one value.

# and with the input i set it up like this : 

class myAttempt:

    # 01 / 21 / 2026 - 7:30 pm

    # A is the list of integers.

    def spike(A):

        A.sort(reverse=True)

        front = []
        back = []

        frontBack = 1

        for idx in range(0, len(A)):
            if frontBack == 1:
                back.append(A[idx])
                frontBack = -1
            else:
                front.append(A[idx])
                frontBack = 1

        front.sort()

        spike = front + back

        spikeLen = 1

        for idx in range(1, len(spike)):
            if spike[idx] == spike[idx - 1]:
                continue
            else:
                spikeLen += 1

        return spikeLen