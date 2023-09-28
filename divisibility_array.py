# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

def divisibility_array(word: str, m: int) -> list[int]:
    i = 0
    num = int(word)
    divisor = 1
    result = []
    while i < len(word):
        if num // divisor % m == 0:
            result.append(1)
        else:
            result.append(0)
        divisor *= 10
        i += 1
    return result[::-1]


def divisibility_array1(word: str, m: int):
    i = 1
    result = []
    while i <= len(word):
        result.append(1 if (int(word[0:i]) % m) == 0 else 0)
        i += 1
    return result


def main():
    print(divisibility_array("12344", 2))
    print(divisibility_array1("12344", 2))


if __name__ == "__main__":
    main()
