

def right_valid_palindrome(string: str) -> bool:

    left, right = 0, len(string) - 1

    while left < right:

        if left < right and not check_symbool(s=string[left]):
            left += 1
        if right > left and not check_symbool(s=string[right]):
            right -= 1

        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

def valid_palindrome(string: str) -> bool:
    left, right = 0, len(string) - 1

    while left < right:
        if left < right and check_symbool(string[left]):
            left += 1
        if left < right and check_symbool(string[right]):
            right -= 1

        if string[left] != string[right]:
            return False

    return True


def check_symbool(s: str) -> bool:
    return ord("a") <= ord(s) <= ord("z") or ord("A") <= ord(s) <= ord("Z") or ord("0") <= ord(s) <= ord("9")


if __name__ == "__main__":
    print(right_valid_palindrome("A man, a plan, a canal: Panama"))
