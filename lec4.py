class NumberSystem3:

    @staticmethod
    def numFrequency(n, data):
        count = 0

        while n > 0:
            lastDig = n % 10

            if lastDig == data:
                count += 1

            n //= 10

        return count

    @staticmethod
    def numFrequencyQueries(n, query):
        ans = [0] * 10

        while n != 0:
            d = n % 10
            n //= 10

            ans[d] += 1

        for q in query:
            print(q, ":", ans[q])

    @staticmethod
    def pow(n):
        pwr = 1

        while n != 0:
            n //= 10
            pwr *= 10

        return pwr

    @staticmethod
    def decimalToBinary(n):
        ans = 0
        power = 1

        while n != 0:
            rem = n % 2
            n //= 2

            ans += rem * power
            power *= 10

        return ans

    @staticmethod
    def binaryToDecimal(n):
        pwr = 1
        ans = 0

        while n != 0:
            rem = n % 10

            ans += rem * pwr
            pwr *= 2
            n //= 10

        return ans

    @staticmethod
    def decimalToAnyBase(n, base):
        pwr = 1
        ans = 0

        while n != 0:
            rem = n % base

            ans += rem * pwr

            n //= base
            pwr *= 10

        return ans

    @staticmethod
    def anyBaseToDecimal(n, base):
        pwr = 1
        ans = 0

        while n != 0:
            rem = n % 10

            ans += rem * pwr

            n //= 10
            pwr *= base

        return ans

    @staticmethod
    def anyBaseToAnyBase(n, b1, b2):
        decimal = NumberSystem3.anyBaseToDecimal(n, b1)

        return NumberSystem3.decimalToAnyBase(decimal, b2)

    @staticmethod
    def anyBaseAddition(n, m, base):
        pwr = 1
        ans = 0
        carry = 0

        while n != 0 or m != 0 or carry != 0:

            sum_val = carry + (n % 10) + (m % 10)

            n //= 10
            m //= 10

            ansLastDig = sum_val % base
            carry = sum_val // base

            ans += ansLastDig * pwr
            pwr *= 10

        return ans

    @staticmethod
    def anyBaseSub(n, m, base):
        pwr = 1
        ans = 0
        borrow = 0

        while n != 0:

            diff = borrow + (n % 10) - (m % 10)

            n //= 10
            m //= 10

            if diff < 0:
                borrow = -1
                diff += base
            else:
                borrow = 0

            ans += diff * pwr
            pwr *= 10

        return ans


# Main
n = int(input())
m = int(input())
base = int(input())

print(NumberSystem3.anyBaseSub(n, m, base))