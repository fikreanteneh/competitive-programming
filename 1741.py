from collections import defaultdict

n = int(input())
def compare(shirt1, shirt2):
    size = {"S": -1, "M": 0, "L": 1} 
    s = {True: "<", False: ">"}
    l = {True: ">", False: "<"}
    if shirt1 == shirt2:
        print("=")
    elif size[shirt1[-1]] < size[shirt2[-1]]:
        print("<")
    elif size[shirt1[-1]] > size[shirt2[-1]]:
        print(">")
    else:
        if shirt1[-1] == "S":
            print(s[len(shirt1) > len(shirt2)])
        else:
            print(l[len(shirt1) > len(shirt2)])
        
for k in range(n):
    shirts = input().split(" ")
    compare(shirts[0], shirts[1])
