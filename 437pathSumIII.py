# https://leetcode.com/problems/path-sum-iii/
# medium

class firstAttempt:

    # 10 / 02 / 2025 - 10:17 pm

    # Runtime -> 1 ms - 93.27%  
    # Memory -> 18.18 MB - 87.96%

    # i put like 4 hours into this problem, i still don't really understand this solution
    # i think if i kept working and i just did the o(n2) i would've gotten it, but man
    # i just couldn't get past it.

    # i asked chatgpt for a hint and it brought up using a hashmap, but i didn't understand
    # how that wasn't o(n2). but basically its using a hashmap and dfs's storing all of the
    # prefix sums.

    # this is chatgpts simple explanation for me cuz wtf :

    # in short it keeps a "running total" as it explores, and uses the hashmap to instantly
    # know if some earlier point in the path makes the curretn s egment add up to the target.

    # i think will more problems ill understand it better, but the hashmap decrement is 
    # messing me up a bit.
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixCount = {0: 1}
        return self.dfs(root, 0, targetSum, prefixCount)

    def dfs(self, node, curSum, targetSum, prefixCount):
        if not node:
            return 0

        curSum += node.val
        res = prefixCount.get(curSum - targetSum, 0)

        prefixCount[curSum] = prefixCount.get(curSum, 0) + 1

        res += self.dfs(node.left, curSum, targetSum, prefixCount)
        res += self.dfs(node.right, curSum, targetSum, prefixCount)

        prefixCount[curSum] -= 1

        return res