# 记录生效，根据年份来判断生肖

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

print(chinese_zodiac[0:4])

print(chinese_zodiac[0:-1])

year = 2022
print(year % 12)
print(chinese_zodiac[year % 12])