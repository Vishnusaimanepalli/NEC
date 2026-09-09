def input_arr(n, val):
    if n == 0:
        return [0] * val

    arr = input_arr(n - 1, val)
    arr[n - 1] = int(input())

    return arr


def print_arr(arr, idx):
    if idx == len(arr):
        return

    print(arr[idx], end="\t")
    print_arr(arr, idx + 1)

def maximum (arr, idx):
    
    
def minimum (arr, idx):

n = int(input())
val = int(input())

arr = input_arr(n, val)
print_arr(arr, 0)