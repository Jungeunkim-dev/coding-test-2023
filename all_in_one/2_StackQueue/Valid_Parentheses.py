def isValid(input):
    s = []

    for char in input:
        if char == "(":
            s.append(")")

        elif char == "[":
            s.append("]")

        elif char == "{":
            s.append("}")

        else:
            if not s:
                return False
            cur = s.pop()
            if cur != char:
                return False

    if not s:
        return True


print(isValid("()"))
