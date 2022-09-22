# -*- coding: utf-8 -*-
print("n = 123")
print("456.789")
print("s2 = \'Hello, \\\'Adam\\\''")

print('%2d-%02d' % (3, 1))
print('growth rate : %d %%' % 7)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('刘建明', 88.88))
r = 2.5
s = 3.14 * r ** 2
print(f'the area of a circle with radius {r} is {s:.2f}')

s1 = 72
s2 = 85
s3 = (s2-s1)/s1*100
print(f'小明的成绩从去年的{s1}升到今年的{s2}，总共提升的百分比为：{(s2-s1)/s1*100:.1f}%')
print('小明的成绩增长了：%.1f %%' % s3)
print('小明的成绩真的增长了{0:.1f}%'.format(s3))



