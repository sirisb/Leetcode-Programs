"""
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.

 Method 1. Use stack to push all nodes, reiterate list, pop from stack and compare if the nodes are same.

 Method 2: Iterate List using 2 pointers, when reached middle, reverse 2nd half of list and compare with first half.

 Method 3: Using recursion stack.
"""


class ListNode:
    def __init__(self, value, nxt=None):
        self.val = value
        self.nxt = nxt


def display_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.val}", end="->")
        curr = curr.nxt


def is_list_palindrome(head):
    curr_stack = head
    stack = []
    while curr_stack is not None:
        stack.append(curr_stack.val)
        curr_stack = curr_stack.nxt

    curr_comp = head
    while curr_comp is not None and len(stack) > 0:
        if stack.pop() != curr_comp.val:
            return False
        curr_comp = curr_comp.nxt
    return True


def create_list():
    curr = None
    head = ListNode(123)
    curr = head
    curr.nxt = ListNode(726)
    curr = curr.nxt
    curr.nxt = ListNode(23)
    curr = curr.nxt
    curr.nxt = ListNode(786)
    curr = curr.nxt
    curr.nxt = ListNode(123)
    curr = curr.nxt
    return head


def main():
    head = create_list()
    display_list(head)
    print(is_list_palindrome(head))


if __name__ == "__main__":
    main()
