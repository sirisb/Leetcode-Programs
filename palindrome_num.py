def is_palindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s_rev = str(x)[::-1]
    if s_rev == str(x):
        return True
    else:
        return False


def main():
    print(is_palindrome(input("Enter Num: ")))


if __name__ == "__main__":
    main()
