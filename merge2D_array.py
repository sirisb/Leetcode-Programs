# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

def merge_arrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    i = j = 0
    result_lst = []
    while i < len(nums1) and j < len(nums2):
        nums1_id, nums1_val = nums1[i]
        nums2_id, nums2_val = nums2[j]
        if nums1_id == nums2_id:
            result_lst.append([nums1_id, nums1_val+nums2_val])
            i += 1
            j += 1
        elif nums1_id < nums2_id:
            result_lst.append(nums1[i])
            i += 1
        else:
            result_lst.append(nums2[j])
            j += 1
    while i < len(nums1):
        result_lst.append(nums1[i])
        i += 1
    while j < len(nums2):
        result_lst.append(nums2[j])
        j += 1
    return result_lst


def main():
    print(merge_arrays([[1, 2], [2, 3], [3, 1], [4, 1]],
                       [[1, 3], [3, 2], [4, 2]]))


if __name__ == "__main__":
    main()

