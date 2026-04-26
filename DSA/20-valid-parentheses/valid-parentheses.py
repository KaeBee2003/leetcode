class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if i == "(":
                a.append(")")
            elif i == "[":
                a.append("]")
            elif i == "{":
                a.append("}")
            elif len(a) != 0 and a[-1] == i:
                a.pop()
            else:
                return False
        return len(a) == 0
