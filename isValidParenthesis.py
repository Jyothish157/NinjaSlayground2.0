def isValidParenthesis(s: str) -> bool:
    # Write your code here
    stack = []
    brace_map = {')':'(','}':'{',']':'['}
    for char in s:
        if char in brace_map.values():
            stack.append(char)
        elif char in brace_map.keys():
            if not stack or stack[-1] != brace_map[char]:
                return False
            stack.pop()

    return len(stack) == 0
