# 2 loops - 1 main loop, 1 inner loop to find the match. for every num in main loop, find the second number that is
# required to meet target sum, and with 2nd loop just check for the number. Can sort beforehand to improve
# efficiency. Further using binary search gives best time complexity. but, order is not preserved.


def two_sum(nums, target):
    for i in range(0, len(nums)):
        if nums[i] < target:
            sec_num = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == sec_num:
                    return i, j


def two_sum1(nums, target):
    num_map = {}
    # put all nums to map.
    for i in range (0, len(nums)):
        num_map[nums[i]] = i
    # find the 2nd num required by evaluating target - 1st num.
    for i in range(0, len(nums)):
        req = target - nums[i]
        if num_map.get(req):
            return i, num_map.get(req)

    return None


def main():
    nums = [2, 3, 1, 5, 20, 17]
    print(two_sum(nums, 45))
    print(*nums, sep="->")

    print(two_sum1(nums, 45))


if __name__ == "__main__":
    main()
