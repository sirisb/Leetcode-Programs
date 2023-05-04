class ListNode:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def merge_two_lists(list1, list2):
    result_list = None
    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            node = list1
            list1 = list1.next
        else:
            node = list2
            list2 = list2.next

        if result_list is None:
            # assign the node as head if it's first.
            result_list = node
            res_head = node
        else:
            result_list.next = node
            result_list = result_list.next

    while list1 is not None and list2 is None:
        result_list.next = list1
        result_list = result_list.next
        list1 = list1.next
    while list1 is None and list2 is not None:
        result_list.next = list2
        result_list = result_list.next
        list2 = list2.next
    return res_head


def create_list(lst):
    curr = None
    head = ListNode(lst[0])
    curr = head
    for index in range(1, len(lst)):
        curr.next = ListNode(lst[index])
        curr = curr.next
    return head


def display_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.value}", end="->")
        curr = curr.next
    print("\n")


def main():
    head1 = create_list([2, 4, 6, 8])
    display_list(head1)
    head2 = create_list([3, 5, 7, 9])
    display_list(head2)
    res_head = merge_two_lists(head1, head2)
    display_list(res_head)


if __name__ == "__main__":
    main()
