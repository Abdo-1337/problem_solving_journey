class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        copy = [c for c in s]
        for i in range(len(s)):

            element = copy.pop(0)
            copy.insert(len(copy), element)
            new = ""
            for ch in copy:
                new += ch
            if new == goal:
                return True
        return False
            