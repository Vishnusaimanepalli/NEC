def diamondOfSpaces(n):
    nsp = 1
    nst = n // 2

    for row in range(1, n + 1):

        for cst in range(1, nst + 1):
            print("*", end="\t")

        for csp in range(1, nsp):
            print("\t", end="")

        for cst in range(1, nst + 1):
            print("*", end="\t")

        if row <= n // 2:
            nsp += 2
            nst -= 1
        else:
            nst += 1
            nsp -= 2

        print("\t")


def diamondOfSpaces2(n):
    nst = (n // 2) + 1
    nsp = 1

    for row in range(1, n + 1):

        for cst in range(1, nst + 1):
            print("*", end="\t")

        for csp in range(1, nsp + 1):
            print("\t", end="")

        for cst in range(1, nst + 1):
            print("*", end="\t")

        if row <= n // 2:
            nsp += 2
            nst -= 1
        else:
            nsp -= 2
            nst += 1

        print("\t")


def HollowSandTimer(n):
    nst = n       # number of columns
    nsp = 0       # leading spaces

    for row in range(1, n + 1):

        # Print leading spaces
        for csp in range(1, nsp + 1):
            print("\t", end="")

        # Print stars and inner spaces
        for col in range(1, nst + 1):

            if row == 1 or row == n or col == 1 or col == nst:
                print("*", end="\t")
            else:
                print("\t", end="")

        print()

        # Update values
        if row <= n // 2:
            nsp += 1
            nst -= 2
        else:
            nsp -= 1
            nst += 2


def arrow(n):
    nsp = n // 2
    nst = 1

    for row in range(1, n + 1):

        for csp in range(1, nsp + 1):

            if row == (n // 2) + 1:
                print("*", end="\t")
            else:
                print("\t", end="")

        for cst in range(1, nst + 1):
            print("*", end="\t")

        if row <= n // 2:
            nst += 1
        else:
            nst -= 1

        print("\t")


def nFactorialTillN(n):
    # n = 5
    #
    # 1
    # 5 25
    # 125 625 3125
    # 15625 78125 390625 1953125
    # ...

    nst = 1
    a = 1

    for row in range(1, n + 1):

        for i in range(1, nst + 1):
            print(a, end="\t")

            product = a * n
            a = product

        nst += 1
        print()


def wPattern(n):
    nst = n

    for row in range(1, n + 1):

        for cst in range(1, nst + 1):

            if cst == 1 or cst == n:
                print("*", end="\t")

            elif row > (n // 2) and (
                row == cst or row + cst == n + 1
            ):
                print("*", end="\t")

            else:
                print("\t", end="")

        print("\t")


def numberDiamond(n):
    nsp = n // 2
    nsd = 1

    for row in range(1, n + 1):

        for csp in range(1, nsp + 1):
            print("\t", end="")

        val = row

        if row > (n // 2) + 1:
            val = n - row + 1

        for csd in range(1, nsd + 1):

            print(val, end="\t")

            if csd <= nsd // 2:
                val += 1
            else:
                val -= 1

        if row <= n // 2:
            nsd += 2
            nsp -= 1
        else:
            nsd -= 2
            nsp += 1

        print("\t")


def numPattern4(n):
    nsp = n - 1
    nst = 1

    for row in range(1, n + 1):

        for csp in range(1, nsp + 1):
            print("\t", end="")

        val = row

        for cst in range(1, nst + 1):

            print(val, end="\t")

            if cst <= nst // 2:
                val += 1
            else:
                val -= 1

        nsp -= 1
        nst += 2

        print("\t")


def numW(n):
    nst = 1
    nsp = (2 * n) - 3

    for row in range(1, n + 1):

        val = 1

        # First side
        for cst in range(1, nst + 1):
            print(val, end="\t")
            val += 1

        # Middle spaces
        for csp in range(1, nsp + 1):
            print("\t", end="")

        # Second side
        for cst in range(1, nst + 1):

            if row == n and cst == 1:
                val -= 1
                continue

            val -= 1
            print(val, end="\t")

        nst += 1
        nsp -= 2

        print()


def binomialPattern(num):
    # Formula:
    # nCr+1 = ((n - r) * nCr) / (r + 1)

    for n in range(0, num):

        nCr = 1

        # 1st value of every row is 1
        for r in range(0, n + 1):

            print(nCr, end="\t")

            nCr1 = ((n - r) * nCr) // (r + 1)
            nCr = nCr1

        print()


# Main
num = int(input())

binomialPattern(num)