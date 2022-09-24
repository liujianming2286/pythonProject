# 记录生效，根据年份来判断生肖

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

print(chinese_zodiac[0:4])

print(chinese_zodiac[0:-1])

year = 2022
print(year % 12)
print(chinese_zodiac[year % 12])

print('狗' in chinese_zodiac)

print(chinese_zodiac * 3)

for year in range(2008, 2023):
    print("%s 年的生肖是 %s" % (year, chinese_zodiac[year % 12]))

