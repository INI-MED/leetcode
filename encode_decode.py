


def encode_str(string: str) -> str:

    res = ""

    for item in string:
        res += "#" + str(len(string)) + item
    return res


def decode_str(string: str) -> str:
    pass

