from collections import deque
def backspaceCompare(s: str, t: str) -> bool:
    def clean(s): 
        stack = deque()
        for c in s:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack

    return clean(s) == clean(t)

print(backspaceCompare("ab#c", "ad#c"))