# 균형잡힌 세상
# 백준/4949번


while True:
    word = input()

    if word == ".":
        break

    stack = []
    for i in word:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop() 
            else:
                stack.append(')')
                break 
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop() 
            else:
                stack.append(']')
                break
    if stack:
        print("no")
    else:
        print("yes")