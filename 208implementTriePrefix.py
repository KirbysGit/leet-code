# https://leetcode.com/problems/implement-trie-prefix-tree/
# medium

class firstAttempt:

    # 11 / 10 / 2025 - 2:03 pm

    # Runtime -> 20 ms - 98.39%
    # Memory -> 30.27 MB - 95.99%'

    # alright htis one had me a bit confused, after cheating basically with mrgpt i remembered
    # this from mr.meades class. but its like how we layer the nodes, with a root node
    # structure then as we add nodes we add them to teh root node structure if its the same
    # prefix, else we add them to child nodes

    # but anyways, i tried to set it up with a general like we can just serach up words
    # i wasn't really even thinking about the node level structure.

    # so i'll put the solution below, then i'll explain it.

    # first off with our init. we just set up a dictionary to store our nodes.

    def __init__(self):
        self.tree = {}

    # then with our insert function, the goal is really just to incrementally
    # move down the levels, add the characters as we go. so like we get the word
    # "app", then we start at root node, and add 'a' to the root node, then 'p' to the child
    # node, then 'p' to the child node of the 'p' node. its like a staircase effect.

    def insert(self, word: str) -> None:
        node = self.tree
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True

    # when we search the word, we're basically following the same staircase effect,
    # but instead we're just checking the characters per level to see if the
    # word we are looking for is valid. then if we get to the end of the word
    # which is declared by our $ character then we know we can return true.

    def search(self, word: str) -> bool:
        node = self.tree
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '$' in node

    # then with our startswith function, its basically the same thing, but
    # instead of checking if we find the $ character to assume the word is
    # done, we just check if we can basically get to the end of the prefix.

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
        