if __name__ == '__main__':
    N = int(input())
 
# class Lists:
#     def __init__(self):
#         self.array = []
#     def appending(self, val):
#         self.array.append(val)
#     def inserting(self, index, val):
#         self.array.insert(index, val)
#     def removing(self, val):
#         self.array.remove(val) 
#     def sorting(self):
#         self.array.sort()
#     def printing(self):
#         print(self.array)
#     def popping(self):
#         self.array.pop()
#     def reversing(self):
#         self.array.reverse()
def lists(N):
    array = []
    for i in range(N):
        inst = input()
        inst = inst.split(" ")
        if inst[0] == "append":
            array.append(eval(inst[1]))
        elif inst[0] == "remove":
            array.remove(eval(inst[1]))
        elif inst[0] == "insert":
            array.insert(eval(inst[1]), eval(inst[2]))  
        elif inst[0] == "sort":
            array.sort()
        elif inst[0] == "print":
            print(array)
        elif inst[0] == "pop":
            array.pop()
        elif inst[0] == "reverse":
            array.reverse()
lists(N)
            
