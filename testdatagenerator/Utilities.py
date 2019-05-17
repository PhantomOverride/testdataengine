import re # Support for regex


def luhn(inString):
    """Calculate and return the luhn number for a string"""
    pattern = re.compile("^[0-9-]+$")
    if not pattern.match(inString):
        raise ValueError('Luhn called with non number value')

    sum = 0
    odd = False
    for s in inString:
        if s == "-":
            continue
        odd = not odd
        if odd:
            temp = str(int(s) * 2)
            for i in temp:
                sum += int(i)
        else:
            sum += int(s)
    sum = str(sum)
    toRet = int(sum[len(sum) - 1])
    return toRet if toRet == 0 else 10 - toRet
