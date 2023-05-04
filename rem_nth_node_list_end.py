class List_node:
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
    head = List_node(lst[0])
    curr = head
    for index in range(1, len(lst)):
        curr.next = List_node(lst[index])
        curr = curr.next
    return head

#  2 pointer method , fast and slow pointers.
#  while loop fast pointer reaches end of list, move 2 nodes at a time and slow ptr will reach mid.
# 


def remove_nth_from_end(head, n):
    slow_ptr = head
    fast_ptr = head
    list_len = 0
    slow_ptr_index = 1
    while fast_ptr is not None:
        fast_ptr = fast_ptr.next.next
        list_len += 2
        slow_ptr = slow_ptr.next
        slow_ptr_index += 1
    print("List Length = ", list_len)
    print("Slow Pointer ", slow_ptr_index)
    if fast_ptr is None:
        if list_len - n == 0:  # remove head of linked list.
            head = head.next
            return head

        if slow_ptr_index > (list_len - n):
            slow_ptr = head
            slow_ptr_index = 1

        while slow_ptr_index < (list_len - n):
            slow_ptr = slow_ptr.next
            slow_ptr_index += 1

        if slow_ptr_index == (list_len - n):
            slow_ptr.next = slow_ptr.next.next  # del the nth node.
    return head


def main():
    head = create_list([2, 4, 6, 8, 9, 14])
    display_list(head)
    head = remove_nth_from_end(head, 6)
    display_list(head)


if __name__ == "__main__":
    main()
