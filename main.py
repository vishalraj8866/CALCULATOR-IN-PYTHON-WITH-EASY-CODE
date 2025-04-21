print("please choose option for to use calculator\n for add press 1\n for subtract press 2\n for multiply  press 3\n for divide press 4")

in_put = int(input()) # this function take input with user in int = integer.
int1 = int(input())
int2 = int(input())
if in_put == 1:
    print("add = ", int1 + int2)
elif in_put == 2:
    print("subtract = ", int1 - int2)
elif in_put == 3:
    print("multiply = ", int1 * int2)
elif in_put == 4:
    print("divide = ", int1 / int2)
else:
    print("we dont know")
