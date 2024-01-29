
from typing import List
from collections import defaultdict

def group(words: List[str]) -> List[List[str]]:
    hash_map =  defaultdict(list)
    for string in words:
        sorted_word = "".join(sorted(string))
        hash_map[sorted_word].append(string)
    return list(hash_map.values())


if __name__ == "__main__":
    print(group(["cat", "tea", "tan", "ate", "nat", "bat"]))


