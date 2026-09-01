def array_list_input(n):
    arr_lst = []

    for i in range(n):
        arr_lst.append(int(input()))

    return arr_lst


def swap(arr_lst, i, j):
    arr_lst[i], arr_lst[j] = arr_lst[j], arr_lst[i]


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def remove_prime_numbers(n):
    arr_lst = array_list_input(n)
    arr_lst1 = []

    i = len(arr_lst) - 1

    while i >= 0:
        if is_prime(arr_lst[i]):
            swap(arr_lst, i, len(arr_lst) - 1)

            removed_elem = arr_lst.pop()
            arr_lst1.append(removed_elem)

        i -= 1

    print(arr_lst)
    print(arr_lst1)
    print("\nFncn DONE")


def remove_prime1(arr_lst):
    ans = []

    for elem in arr_lst:
        if not is_prime(elem):
            ans.append(elem)

    # Clear original list
    arr_lst.clear()

    # Add non-prime elements back
    for elem in ans:
        arr_lst.append(elem)

    print(arr_lst)