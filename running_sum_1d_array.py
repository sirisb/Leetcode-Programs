def running_sum1(nums):
    total = 0
    for i in range(0, len(nums)):
        total += nums[i]
        nums[i] = total


# List comprehension.
def running_sum(nums):
    return [sum(nums[:i+1]) for i in range(1, len(nums))]


if __name__ == "__main__":
    num_arr = [1, 3, 2, 10, 4]
    running_sum1(num_arr)
    print(num_arr)

    print("  ", running_sum(num_arr))

