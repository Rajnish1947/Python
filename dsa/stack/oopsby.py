
# by opps concept


class Stack:
    def __init__(self):
        self.stack = []

    # Push element into stack
    def push(self, x):
        self.stack.append(x)

    # Pop element from stack
    def pop(self):
        if len(self.stack) == 0:
            return None
        x = self.stack.pop()
        return x

    # Get the top (last) element
    def last(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    # Get size of stack
    def size(self):
        return len(self.stack)

    # Display stack nicely when printed
    def __str__(self):
        return f"Stack: {self.stack}"


# ---------- Test the stack ----------
stack = Stack()
stack.push(3)
stack.push(2)
stack.push(1)

print(stack)           # shows full stack
print("Top element:", stack.last())
print("Popped:", stack.pop())
print(stack)
print("Size:", stack.size())
