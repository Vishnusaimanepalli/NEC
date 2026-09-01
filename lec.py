def fiboPattern(n):
    a = 0
    b = 1
    temp = 0

    for row in range(1, n + 1):
        for i in range(1, row + 1):
            print(a, end="\t")

            temp = a + b
            a = b
            b = temp

        print()


def pythagoreanTriplet(a, b, c):
    max_val = max(a, b, c)

    if max_val == a and b * b + c * c == a * a:
        return True
    elif max_val == b and a * a + c * c == b * b:
        return True
    elif max_val == c and b * b + a * a == c * c:
        return True
    else:
        return False


def pythagoreanTriplet2(a, b, c):
    return (
        b * b + c * c == a * a
        or a * a + c * c == b * b
        or b * b + a * a == c * c
    )


def pow(n):
    pwr = 1

    while n != 0:
        n //= 10
        pwr *= 10

    return pwr


def digitsInForward(n):
    power = pow(n)
    power //= 10

    while power > 0:
        quo = n // power
        n %= power
        power //= 10

        print(quo)


def checkPrime(n):
    res = False

    for i in range(2, n // 2 + 1):
        if n % i != 0:
            res = True
        else:
            return False

    return res


def isaPrimeNum(n):
    res = checkPrime(n)

    if res == True:
        print("It is prime number.")
    else:
        print("It is not prime number.")


def countDigit(n):
    count = 0

    while n != 0:
        n //= 10
        count += 1

    return count


def rotateNumber(n, r):
    countDig = countDigit(n)

    r %= countDig

    if r < 0:
        r += countDig

    div = 1
    mul = 1

    for i in range(1, countDig + 1):
        if i <= r:
            div *= 10
        else:
            mul *= 10

    a = n % div
    b = n // div

    return a * mul + b


def benjaminBulb(n):
    i = 1

    while i * i <= n:
        print(i * i)
        i += 1


def inverseOfNumber(n):
    inv = 0
    orgPos = 1

    while n != 0:
        orgDig = n % 10
        invDig = orgPos
        invPos = orgDig

        inv += invDig * (10 ** (invPos - 1))

        n //= 10
        orgPos += 1

    print(inv)



n = int(input())
inverseOfNumber(n)