"""
Print all prime numbers within the given number.
1 isn't a prime num as it's the only factor.
2 for loops
    1 loop to loop through number between 2 to n.
    2nd loop in checking whether the passed num is prime, to divide the num from all numbers between 2 to (num/2)+1.
    num/2+1 because, only division possibility needs to be checked until half of the num to
    check if it is a prime number.

"""


def main():
    primes(int(input("Enter a num: ")))


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, round(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def primes(num):
    prime_list = []
    if num < 2:
        print("No prime numbers.")
        return
    if num >= 3:
        prime_list.append(2)
        prime_list.append(3)
    if num == 2:
        prime_list.append(2)
    for i in range(4, num + 1):
        if is_prime(i):
            prime_list.append(i)

        # append to list if prime.
        # continue if not.
    return prime_list


if __name__ == "__main__":
    main()
