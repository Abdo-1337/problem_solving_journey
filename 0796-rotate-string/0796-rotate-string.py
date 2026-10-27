class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_copy = [c for c in s]
        goal_copy = [c for c in goal]

        for i in range(len(s)):

            element = s_copy.pop(0)
            s_copy.insert(len(s_copy), element)
            if s_copy == goal_copy:
                return True
        return False
            