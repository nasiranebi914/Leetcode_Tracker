# Last updated: 7/8/2025, 10:03:58 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hash = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        res = []
        l = []
        for d in digits:
            l.append(hash[int(d)])

        def backtrack(start, path):
            # base case
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return
            
            for char in l[start]:
                # choose
                path.append(char)
                # explore
                backtrack(start+1, path)
                # undo
                path.pop()
        backtrack(0,[])
        return res
