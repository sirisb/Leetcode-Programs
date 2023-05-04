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


def main():
    nums = [2, 3, 1, 5, 20, 17]
    print(two_sum(nums, 19))
    print(*nums, sep="->")


if __name__ == "__main__":
    main()
