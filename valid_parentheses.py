def is_valid(s):
    stack = []
    # if opening bracket push to stack.
    # if closing bracket, if stack is empty, return invalid.
    # if stack has items, check for matching starting bracket from stack.pop. return invalid if no match found in stack.
    for c in s:
        if c in ("{", "[", "("):
            stack.append(c)
            continue
        if stack and c in ("]", "}", ")"):
            p = stack.pop()
            if c == "}" and p != "{":
                return False
            elif c == "]" and p != "[":
                return False
            elif c == ")" and p != "(":
                return False
        elif not stack and c in ("]", "}", ")"):
            return False
    if stack:  # stack has items if ending bracket doesn't exist.
        return False

    return True


def main():
    print(is_valid(input("Enter a string with parenthesis: ")))


if __name__ == "__main__":
    main()
