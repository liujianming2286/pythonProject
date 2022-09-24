# 打开文件
import os

f = open('C:\\Users\\ljm65\\Desktop\\新建文本文档.txt', 'r', encoding='utf-8')
# 读取一遍后，后续不能再次读取
# content = f.read()
# print(content)
contents = f.readlines()
for i in range(len(contents)):
    contents[i] = str(i+1) + ':' + contents[i]
print(contents)
f.close()

# 写入新的文件
# os.mkdir("C:\\Users\\ljm65\\Desktop\\拷贝.txt")
fp = open('E:\\python\\pythonProject\\cainiao\\test\\拷贝.txt', 'w', encoding='utf-8')
fp.writelines(contents)
fp.close()


# 把文件读取文件抽象成一个方法
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f1:
        read_lines_from_file = f1.readlines()
        return read_lines_from_file
# 把写文件抽象成一个函数


def write_file(content: list = (), target_write_file=str()):
    with open(target_write_file, 'w', encoding='utf-8') as f2:
        for line3 in content:
            f2.write(line3)


new_lines = []

# 遍历列表，把每一行加上下标
for index, line in enumerate(read_file('C:\\Users\\ljm65\\Desktop\\新建文本文档.txt')):
    new_lines.append(line)

# write_file(new_lines, 'test\\拷贝345.txt')

# os.remove("test\\拷贝345.txt")
