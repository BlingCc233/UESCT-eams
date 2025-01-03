import json
import os
import random
import re

pattern = re.compile(r'^uestc-\d{4}-\d{2}-\d{2}\.json$')

dir = "/Users/ccbling/tmp"

for filename in os.listdir(dir):
    if pattern.match(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)


typography = {}


for item in data:
    if item.get('MuiTypography-root') == None or item.get('rich-text-content') == None:
        continue
    if item['MuiTypography-root'] not in typography:
            typography[item['MuiTypography-root']] = []
            typography[item['MuiTypography-root']].append(item['rich-text-content'])
            continue
    typography[item['MuiTypography-root']].append(item['rich-text-content'])

typography_list = []

# 把键值对转换为列表
for key, value in typography.items():
    if key != 'BlingCc':
        typography_list.append({key : value})

# 把列表shuffle五次
for i in range(5):
    random.shuffle(typography_list)

# 从列表中随机取出1个元素
print(random.choice(typography_list))