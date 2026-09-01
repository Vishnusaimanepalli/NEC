def odd_left_even_right(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] *= -1

    arr.sort()

    idx = 0
    while idx < len(arr) and arr[idx] < 0:
        arr[idx] *= -1
        idx += 1

    return arr

def state_of_wakanda1(arr):
    n = len(arr)
    m = len(arr[0])

    for j in range(m):
        if j % 2 == 0:
            for i in range(n):
                print(arr[i][j], end="\t")
        else:
            for i in range(n - 1, -1, -1):
                print(arr[i][j], end="\t")

        print()

def state_of_wakanda2(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                print(arr[i][j], end="\t")
        else:
            for j in range(m - 1, -1, -1):
                print(arr[i][j], end="\t")

        print()

def state_of_wakanda3(arr):
    n = len(arr)
    m = len(arr[0])

    for gap in range(m):
        i = 0
        j = gap

        while i < n and j < m:
            print(arr[i][j], end="\t")
            i += 1
            j += 1

        print()


def state_of_wakanda5_spiral(arr):
    n = len(arr)
    m = len(arr[0])
    tnel = n * m

    rmin = 0
    rmax = n - 1
    cmin = 0
    cmax = m - 1

    while tnel > 0:

        for r in range(rmin, rmax + 1):
            if tnel == 0:
                break
            print(arr[r][cmin], end=" ")
            tnel -= 1
        print()
        cmin += 1

        for c in range(cmin, cmax + 1):
            if tnel == 0:
                break
            print(arr[rmax][c], end=" ")
            tnel -= 1
        print()
        rmax -= 1

        for r in range(rmax, rmin - 1, -1):
            if tnel == 0:
                break
            print(arr[r][cmax], end=" ")
            tnel -= 1
        print()
        cmax -= 1

        for c in range(cmax, cmin - 1, -1):
            if tnel == 0:
                break
            print(arr[rmin][c], end=" ")
            tnel -= 1
        print()
        rmin += 1
        




