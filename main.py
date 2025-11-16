import keyword

# 读取原文件内容
with open('random_int.py', 'r') as file:
    content = file.read()

# 处理内容：小写转大写（保留字中的小写除外）
processed_content = ''
for char in content:
    # 判断字符是否是小写字母且不是保留字中的小写字母
    if char.islower() and char not in [kw.lower() for kw in keyword.kwlist]:
        processed_content += char.upper()
    else:
        processed_content += char

# 将处理后的内容写入新文件
with open('converted_random_int.py', 'w') as new_file:
    new_file.write(processed_content)
