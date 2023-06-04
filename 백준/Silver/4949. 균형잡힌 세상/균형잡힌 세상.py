while 1:
    line = input()
    stack = []

    if line == ".":
        break

    for i in line:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                continue
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                continue
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
