class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_br = ["{", "(", "["]
        for br in s:
            if br not in open_br and len(stack) == 0 :
                return False
            if br in open_br:
                stack.append(br)
                continue
            if (
                (stack[-1] == "(" and br == ")")
                or (stack[-1] == "{" and br == "}")
                or (stack[-1] == "[" and br == "]")
            ):
                stack.pop()
            else :
                return False
        
        return False if len(stack) > 0 else True
