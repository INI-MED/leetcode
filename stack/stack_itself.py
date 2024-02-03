from typing import Any


class Stack:

    def __init__(self):
        self.minimum_stack = []
        self.stack = []

    def push(self, value: Any) -> None:
        self.stack.append(value)
        value = min(value, self.minimum_stack[-1] if self.minimum_stack else value)
        self.minimum_stack.append(value)

    def pop(self) -> Any:
        res = self.stack.pop()
        self.minimum_stack.pop()
        return res

    def get_min(self) -> Any:
        return self.minimum_stack[-1] if self.minimum_stack else None

    def get_top(self) -> Any:
        return self.stack[-1] if self.stack else None
