def brackets(expression):
    stack = []
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    opening_brackets = set(bracket_pairs.values())
    closing_brackets = set(bracket_pairs.keys())

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0