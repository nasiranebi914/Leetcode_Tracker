# Last updated: 6/17/2025, 10:35:11 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []

        for i in s:
            match i:
                case "" | ".":
                    continue  # skip empty parts and current dir
                case "..":
                    if stack:
                        stack.pop()
                    # else: do nothing; stay at root
                case _:
                    stack.append(i)  # just append the dir name (no "/")

        return "/" + "/".join(stack)