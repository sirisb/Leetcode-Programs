import numpy as np


def shift_array(arr, i, k):
    for j in range(i, k-1):
        arr[j] = arr[j+1]
    return arr


def remove_dupes(arr):
    prev = None
    k = len(arr)
    i = 0
    while i < k:
        if arr[i] == prev:
            arr = shift_array(arr, i, k)
            k -= 1
        else:
            prev = arr[i]
            i += 1
    return arr, k


def main():
    arr = np.array([3, 3, 3, 3, 4, 5, 6])
    print(arr)
    arr, k = remove_dupes(arr)
    print(arr, k)


if __name__ == "__main__":
    main()