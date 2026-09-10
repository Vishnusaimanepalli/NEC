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


def maximum(arr, idx):
    if idx == len(arr):
        return -10**9

    max_value = maximum(arr, idx + 1)

    return max(max_value, arr[idx])


def minimum(arr, idx):
    if idx == len(arr):
        return 10**9

    min_value = minimum(arr, idx + 1)

    return min(min_value, arr[idx])


def find(arr, idx, data):
    if (idx == len(arr)):
        return False
    
    if (arr[idx] == data):
        return True
    
    return find(arr, idx + 1, data)
    
    
def first_idx(arr, i, data):
    if i == len(arr):
        return -1

    if arr[i] == data:
        return i

    return first_idx(arr, i + 1, data)


def last_idx(arr, i, data):
    if i == len(arr):
        return -1

    rec_ans = last_idx(arr, i + 1, data)

    if rec_ans != -1:
        return i

    if arr[i] == data:
        return i

    return -1


def count_of_elem(arr, i, data):
    if i == len(arr):
        return 0

    count = count_of_elem(arr, i + 1, data)

    if arr[i] == data:
        count += 1

    return count


def all_idx(arr, i, data, count):
    if i == len(arr):
        return [0] * count

    if arr[i] == data:
        count += 1

    ans = all_idx(arr, i + 1, data, count)

    if arr[i] == data:
        ans[count - 1] = i

    return ans


def first_and_last_idx(arr, i, data, ans):
    if i == len(arr):
        return False

    if arr[i] == data:
        ans[0] = i

    res = first_and_last_idx(arr, i + 1, data, ans)

    if res:
        return True

    if arr[i] == data:
        ans[1] = i
        return True

    return False

def sub_seq(string):
    
    
# Get KPC number against characters.
#  "0" -> ".;"
#  "1" -> "abc" 
#  "2" -> "def" 
#  "3" -> "ghi" 
#  "4" -> "jkl" 
#  "5" -> "mno" 
#  "6" -> "pqrs" 
#  "7" -> "tu" 
#  "8" -> "vwx"
#  "9" -> "yz"
def get_kpc(string):
    
    
n = int(input())
val = int(input())

arr = input_arr(n, val)

print_arr(arr, 0)
print()

print("Maximum:", maximum(arr, 0))
print("Minimum:", minimum(arr, 0))

data = int(input())

print("Found:", find(arr, 0, data))