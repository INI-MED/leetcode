

def valid_pairs(pairs: str) -> bool:
    """
    algorithm is simple. We need to use stack in order to remove last bracket if we see that its closed.
    To check if bracket has its closing pair we will use hash map with brackets "close": "open".
    While iterating through string we will find that our stack is empty and last element in stack is not opening bracket --> False.
    Otherwise --> we pop from stack until its empty and then return True
    :param pairs: string with parentheses
    :return: boolean
    """

    stack = []
    hash_pairs = {"}": "{", "]": "[", ")": "("}

    for char in pairs:

        if char in hash_pairs:
            # ERROR: getting last symbol from stack, not original string
            if stack and stack[-1] == hash_pairs[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False


if __name__ == '__main__':
    f = valid_pairs("((()))")
    print(f)