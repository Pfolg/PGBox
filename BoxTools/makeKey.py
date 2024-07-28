# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   makeKey |User    Pfolg
# 2024/7/15   22:31
import hashlib

key = "你好，世界！"  # 全角
# 假设我们有一个字符串
original_string = input("输入密码:")

# 选择一个哈希算法，比如MD5
hash_object = hashlib.sha256(original_string.encode())

# 获取十六进制格式的哈希值
hex_dig = hash_object.hexdigest()

print(hex_dig,type(hex_dig))  # 输出哈希值
"fa65d94b3532d83fd24ada92dadecfc7ae5370e6dbf762133027a89c2e7202f1"
