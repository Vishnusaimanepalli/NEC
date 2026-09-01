def palindrome_string(s, si, ei):
    while si < ei:
        if s[si] != s[ei]:
            return False

        si += 1
        ei -= 1

    return True


def print_all_palindromic_substring(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            if palindrome_string(s, i, j):
                sub_str = s[i:j + 1]
                print(sub_str, end="")

            print()