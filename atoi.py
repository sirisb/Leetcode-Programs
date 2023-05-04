def main():
    print(my_atoi(input("Enter string: ")))


def my_atoi(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    is_negative = False
    if len(s) > 200 or len(s) < 1:
        print("Invalid Input length")
        return 0
    if s.startswith("-"):
        is_negative = True
        s = s[1::]
    elif s.startswith("+"):
        s = s[1::]
    res = ""
    for c in s:
        if c.isdigit():
            res += c
        else:
            break

    if len(res) < 1:
        return 0
    if is_negative:
        res_int = -1 * int(res)
    else:
        res_int = int(res)
    if res_int < -2147483648:
        return -2147483648
    elif res_int > 2147483647:
        return 2147483647
    else:
        return res_int


if __name__ == "__main__":
    main()
