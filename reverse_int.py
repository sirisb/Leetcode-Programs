import time
import sys


def main():
    num = int(input("Enter num "))
    print("reverse=", reverse(num))
    # print("reverse1=",reverse1(num))
    # print("reverse2=",reverse2(num))


# Fastest
def reverse(num):
    start = time.perf_counter()
    str_num = str(num)
    is_negative = False
    if str_num[0] == "-":
        num_str = str_num[:0:-1]
        is_negative = True
    else:
        num_str = str_num[::-1]
    print(num_str)
    end = time.perf_counter()
    # print(f"time took is {end - start}")

    if is_negative:
        res = int("-" + num_str)
    else:
        res = int(num_str)
    if res > 2147483648 or res < -2147483648:
        return 0
    return res


def reverse2(num):
    start = time.perf_counter()
    rev = 0
    while num != 0:
        temp = num % 10
        rev = rev * 10 + temp
        num //= 10
    end = time.perf_counter()
    print(f"time took is {end - start}")
    return rev


def reverse1(num):
    start = time.perf_counter()
    num_str = "".join(reversed(str(num)))
    end = time.perf_counter()
    print(f"time took is {end - start}")
    return int(num_str)


main()
