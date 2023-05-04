"""Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# pick the mid node by 2 pointer method.
# reverse the list from mid node to end, reverse second half of list starting from mid.
# reorder by using both main list and second half list, and "set last node to None when second list exhausts".


class ListNode:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def display_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.value}", end="->")
        curr = curr.next
    print("\n")


def create_list(lst):
    curr = None
    head = ListNode(lst[0])
    curr = head
    for index in range(1, len(lst)):
        curr.next = ListNode(lst[index])
        curr = curr.next
    return head


def mid_node(head):
    slow = fast = head
    prev = None
    while fast.next is not None and fast.next.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    return slow.next


def reorder(head):
    mid = mid_node(head)
    head_sec_half = reverse_list(mid)
    curr = head
    # reorder below
    while head_sec_half is not None:
        temp = curr.next
        curr.next = head_sec_half
        head_sec_half = head_sec_half.next
        curr.next.next = temp
        curr = curr.next.next
    curr.next = head_sec_half  # IMPORTANT nullify the end of list.
    return head


def reverse_list(mid):
    curr = mid
    prev = nxt = None
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    display_list(prev)
    return prev


def main():
    head = create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    head = reorder(head)
    display_list(head)


if __name__ == "__main__":
    main()
