def input2(arr):

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input())

    return arr

def lucky_number(arr):

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):

        min_value = arr[i][0]
        col = 0

        for j in range(1, cols):
            if arr[i][j] < min_value:
                min_value = arr[i][j]
                col = j

        lucky = True

        for k in range(rows):
            if arr[k][col] > min_value:
                lucky = False
                break

        if lucky:
            print(min_value)
                        
def exit_point_of_matrix(arr):

    n = len(arr)
    m = len(arr[0])

    i = 0
    j = 0
    direction = 0

    while True:

        direction = (direction + arr[i][j]) % 4

        # East
        if direction == 0:
            j += 1
            if j == m:
                print(i, j - 1)
                break

        # South
        elif direction == 1:
            i += 1
            if i == n:
                print(i - 1, j)
                break

        # West
        elif direction == 2:
            j -= 1
            if j == -1:
                print(i, j + 1)
                break

        # North
        elif direction == 3:
            i -= 1
            if i == -1:
                print(i + 1, j)
                break       
            
def diagonalDiff(arr):
    n = len(arr)
    m = 0
    k = 0
    
    for i in range(n):
        m += arr[i][i]
        k += arr[i][n - i - 1]
        
    return (m - k)

def halfUpperDiagonal(arr):

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

# State of Wakanda 4 - Diagonals of full matrix
def state_of_wakanda4(arr):
    n = len(arr)
    m = len(arr[0])

    for gap in range(n - 1, 0, -1):
        for i in range(gap, n):
            j = i - gap

            if j < m:
                print(arr[i][j], end="\t")
        print()

    for gap in range(m):
        for i in range(n):
            j = i + gap

            if j < m:
                print(arr[i][j], end="\t")
        print()


# Exit Point of Matrix
def exit_point_of_matrix(arr):
    n = len(arr)
    m = len(arr[0])

    i = 0
    j = 0
    direction = 0

    while True:
        direction = (direction + arr[i][j]) % 4

        if direction == 0:
            j += 1

            if j == m:
                print(i, j - 1)
                break

        elif direction == 1:
            i += 1

            if i == n:
                print(i - 1, j)
                break

        elif direction == 2:
            j -= 1

            if j == -1:
                print(i, j + 1)
                break

        elif direction == 3:
            i -= 1

            if i == -1:
                print(i + 1, j)
                break


# Swap two elements in a 2D matrix
def swap(arr, i1, j1, i2, j2):
    arr[i1][j1], arr[i2][j2] = arr[i2][j2], arr[i1][j1]


# Rotate 2D Matrix by 90 Degrees
def rotate_2d_90_deg(arr):
    n = len(arr)
    m = len(arr[0])

    si = 0
    ei = m - 1

    # Transpose
    for i in range(n):
        for j in range(i, m):
            swap(arr, i, j, j, i)

    # Reverse columns
    while si < ei:
        for i in range(n):
            swap(arr, i, si, i, ei)

        si += 1
        ei -= 1

    # Print matrix
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()


# Find maximum element's row index in a column
def max_in_col(arr, c):
    max_val = -10**9
    r = -1

    for i in range(len(arr)):
        if arr[i][c] > max_val:
            max_val = arr[i][c]
            r = i

    return r


# Saddle Point
def saddle_point(arr):
    flag = False

    for i in range(len(arr)):
        min_val = 10**9
        c = -1

        # Find minimum element in current row
        for j in range(len(arr[0])):
            if arr[i][j] < min_val:
                min_val = arr[i][j]
                c = j

        # Find maximum element in that column
        r = max_in_col(arr, c)

        if r == i:
            print(arr[r][c])
            flag = True

    if not flag:
        print("Invalid input")


