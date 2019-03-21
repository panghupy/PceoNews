import csv

# # 读取csv文件
csvfile = open('cookie.csv', 'r')

reader = csv.reader(csvfile)
data = []
for line in reader:
    data.extend(line)
print('s_pvi：' + data[-1])

csvfile.close()
