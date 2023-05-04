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


def reverse_list(head):
    curr_node = head
    prev = None
    next_node = None
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev
        prev = curr_node
        curr_node = next_node
    head = prev
    return head


def create_list(lst):
    curr = None
    head = ListNode(lst[0])
    curr = head
    for index in range(1, len(lst)):
        curr.next = ListNode(lst[index])
        curr = curr.next
    return head


def main():
    head = create_list([2, 4, 6, 8, 9, 14])
    head = reverse_list(head)
    display_list(head)


if __name__ == "__main__":
    main()
