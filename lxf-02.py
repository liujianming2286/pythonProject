# list数组
classmates = ['Michael', 'John', 'Tracy']
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])

classmates.append(['John', 'Tracy'])
print(len(classmates))
print(classmates[0])
print(classmates[-1])

classmates.insert(1, 'ljm')
print(classmates[1])

classmates.pop(1)

# tuple 类型

t = ('a', 'b', 'c', 'd', 'e', ['A', 'B'])
print(t[-1])
t[5][0] = 'X'
t[5][1] = 'Y'
print(t[-1])

# for循环
for i in range(0, len(classmates)):
    print(i)
    print(classmates[i])

for name in classmates:
    print(name)

# 计算 1到1000之和
s = list(range(1000))
print(s)

sum = 0
for s1 in s:
    sum = sum + s1
    print("sum=", sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print("sum=", sum)

