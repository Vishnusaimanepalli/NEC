def input_map(n):
    map_data = {}

    for i in range(n):
        map_data[i] = int(input())

    return map_data


def display(map_data):
    for key, value in map_data.items():
        print(f"{key}: {value}")


def display_gen(map_data):
    for key, value in map_data.items():
        print(f"{key}: {value}")


def arr_to_map(n):
    arr = []

    for i in range(n):
        arr.append(int(input()))

    return arr


def count_freq(arr):
    map_data = {}

    for i in range(len(arr)):
        value = arr[i]

        if value in map_data:
            map_data[value] += 1
        else:
            map_data[value] = 1

    return map_data


def non_repeating_387(arr_lst):
    freq = {}

    # Count frequency
    for value in arr_lst:
        freq[value] = freq.get(value, 0) + 1

    # Find first non-repeating element
    for value in arr_lst:
        if freq[value] > 1:
            continue
        else:
            print(value)
            break


def find_duplicate_442(nums):
    freq = {}
    duplicate_elem = -1

    # Count frequency
    for elem in nums:
        freq[elem] = freq.get(elem, 0) + 1

    # Find duplicate
    for elem in nums:
        if freq[elem] > 1:
            duplicate_elem = elem

    return duplicate_elem



# main
n = int(input())

display_gen(count_freq(arr_to_map(n)))