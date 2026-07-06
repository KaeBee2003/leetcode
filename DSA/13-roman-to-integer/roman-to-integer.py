class Solution:
    def romanToInt(self, s: str) -> int:
        c = []
        for i in s:
            if i == 'I':
                c.append(1)
            elif i == 'V':
                c.append(5)
            elif i == 'X':
                c.append(10)
            elif i == 'L':
                c.append(50)
            elif i == 'C':
                c.append(100)
            elif i == 'D':
                c.append(500)
            elif i == 'M':
                c.append(1000)
            else:
                raise Exception("Unknown Character")
        v = 0
        for i in range(len(c)-1):
            if c[i] < c[i+1]:
                v -= c[i]
            else:
                v += c[i]
        v += c[-1]
        return v