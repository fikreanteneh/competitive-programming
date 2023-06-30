# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
student1 = input().split(" ")
student1 =set(student1)
m= input()
student2 = input().split(" ")
student2 =set(student2)
print(len(student1.difference(student2)))
