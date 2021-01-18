# CPS305 Fall 2020
# Lab 4 Q3
# Yong Kang He
# 500570639

# return a boolean indicating whether the input string has matchin parentheses
# the input string will only consist of ( and ) characters
def hasMatchingParens(str):
    # Your code here
    left = "({["
    right = ")}]"
    S = []
    for c in str:
        if c in left:
            S.append(c)
        elif c in right:
            if S == []:
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S == []


# DO NOT EDIT THE FOLLOWING CODE
# Should be true
print(hasMatchingParens(""))
print(hasMatchingParens("()"))
print(hasMatchingParens("(())"))
print(hasMatchingParens("()()"))
print(hasMatchingParens("(()(()))(())"))

# Should be false
print(hasMatchingParens(")("))
print(hasMatchingParens("())("))
print(hasMatchingParens("(())()))(())"))
print(hasMatchingParens("()()()((()()))()(()"))
print(hasMatchingParens("()()()((())))()(()"))



