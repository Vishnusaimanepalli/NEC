def string_compression(string):
    n = len(string)
    i = 1
    ans = string[0]

    while i < n:
        while i < n and ans[-1] == string[i]:
            i += 1

        if i < n:
            ans += string[i]
            i += 1

    print(ans)


def string_compression_counts(string):
    n = len(string)
    i = 1
    count = 0
    ans = string[0]

    while i < n:
        count = 1

        while i < n and ans[-1] == string[i]:
            i += 1
            count += 1

        if count >= 1:
            ans = ans + ":" + str(count) + "\n"

        if i < n:
            ans += string[i]

        i += 1

    print(ans)


def count_of_hi(s):
    length = len(s)
    i = 0
    count = 0

    s = s.lower()

    while i < length - 1:
        if s[i] == 'h' and s[i + 1] == 'i':
            count += 1
            i += 2
        else:
            i += 1

    print(count)
    
    
def count_of_hi_in_hit(s):
    length = len(s)
    i = 0
    count = 0

    while i < length - 1:
        if s[i] == 'h' and s[i + 1] == 'i':

            if i + 2 < length and s[i + 2] == 't':
                i += 3
            else:
                count += 1
                i += 2

        else:
            i += 1

    return count


def remove_hi(s):
    str1 = ""
    length = len(s)
    i = 0

    while i < length:

        if i + 1 < length and s[i] == 'h' and s[i + 1] == 'i':

            if i + 2 < length and s[i + 2] == 't':
                str1 += "hi"
                i += 2
            else:
                i += 2

        else:
            str1 += s[i]
            i += 1

    print(str1)
    
    
def remove_hit(s):
    str1 = ""
    length = len(s)
    i = 0

    while i < length:

        if (i + 2 < length and
            s[i] == 'h' and
            s[i + 1] == 'i' and
            s[i + 2] == 't'):

            i += 3

        else:
            str1 += s[i]
            i += 1

    print(str1)