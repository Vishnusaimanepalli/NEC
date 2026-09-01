def reverse_order(n):
    while n != 0:
        ans = n % 10
        print(ans)
        n //= 10
        
        
def power(n):
    pow = 1
    while n != 0:
        n //= 10
        pow *= 10
    return pow // 10


def forward_order(n):
    pow = power(n)

    while n != 0:
        ans = n // pow
        print(ans)
        n %= pow
        pow //= 10
        
        
def count_digit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


def rotate_number(n, r):
    count_dig = count_digit(n)

    r %= count_dig
    if r < 0:
        r += count_dig

    div = 1
    mul = 1

    for i in range(1, count_dig + 1):
        if i <= r:
            div *= 10
        else:
            mul *= 10

    a = n % div
    b = n // div

    return a * mul + b

def inverse_of_number(n):
    inv = 0
    org_pos = 1

    while n != 0:
        org_dig = n % 10
        inv_dig = org_pos
        inv_pos = org_dig

        inv += inv_dig * (10 ** (inv_pos - 1))

        n //= 10
        org_pos += 1

    print(inv)
