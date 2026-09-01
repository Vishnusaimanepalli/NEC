
def scoreOfStringLeetCode3110(self, s: str) -> int:
    score = 0

    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))

        return score



def hasAdjacentDigitDifference3931(self, n: int) -> bool:
        s = str(abs(n))

        for i in range(len(s) - 1):
            digit1 = int(s[i])
            digit2 = int(s[i + 1])

            if abs(digit1 - digit2) != 1:
                return False

        return True


def funnyStringHackerRank(s):
    reverse = s[::-1]

    for i in range(len(s) - 1):
        forward = abs(ord(s[i]) - ord(s[i + 1]))
        backward = abs(ord(reverse[i]) - ord(reverse[i + 1]))

        if forward != backward:
            return "Not Funny"

    return "Funny"



def superReducedStringHackerRank(s):
    sb = []

    for ch in s:
        if len(sb) > 0 and sb[-1] == ch:
            sb.pop()
        else:
            sb.append(ch)

    if len(sb) == 0:
        return "Empty String"

    return "".join(sb)



