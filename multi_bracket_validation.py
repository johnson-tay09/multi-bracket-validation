class InvalidOperationError(Exception):
    pass

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        # new node on top of stack gets next value of previous top stack node
        node.next = self.top
        # new node becomes top
        self.top = node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top:
            return False
        return True
        # (return not self.top) most pythonic

    def peek(self):
        if not self.top:
            raise InvalidOperationError(
                "Method not allowed on empty collection")
        return self.top.value


def validate_string(string):
    stack = Stack()
    # opening symbols
    opening = '{[('
    # closing symbols, must be in the matched order of opening
    closing = '}])'
    # iterate through the string we are testing
    for char in string:
        # if we encounter an opening symbol, push it to the stack
        if char in opening:
            stack.push(char)
        # if we encounter a closing symbol, check if it matches the top of the stack
        elif char in closing:
            i = closing.index(char)
            if stack.is_empty() or stack.pop() != opening[i]:
                return False
    # if we've not matched all the symbols... fail!
    if not stack.is_empty:
        return False
    # we have matched all the symbols, success!
    return True
