def input_matrix(n, m):
    arr = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input()))
        arr.append(row)

    return arr


def display(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()

def minimum(arr):
    min_elem = 10**9
    row = len(arr)
    col = len(arr[0])

    for i in range(row):
        for j in range(col):
            min_elem = min(arr[i][j], min_elem)

    return min_elem


def maximum(arr):
    row = len(arr)
    col = len(arr[0])
    max_elem = -10**9

    for i in range(row):
        for j in range(col):
            max_elem = max(max_elem, arr[i][j])

    return max_elem


def find_data_in_matrix(arr, data):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            if data == arr[i][j]:
                print(f"({i} , {j})")
                

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


# Main
n = int(input())
m = int(input())

matrix = input_matrix(n, m)
display(matrix)