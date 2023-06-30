# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
# integers = (int(value) for value in input().split())
integers = tuple(map(int, input().split(" ")))
print( hash(integers) )
