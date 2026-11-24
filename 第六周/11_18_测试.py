import hashlib

"""my_str1 = "这是一段测试文字"

hash_obj = hashlib.sha256()
hash_obj.update(my_str1.encode("utf-8"))

hash_mystr1 = hash_obj.hexdigest()

print(f"原始数据：{my_str1}")
print(f"SHA-256 哈希值：{hash_mystr1}")"""

my_str1 = "这是一"
my_str2 = "段测试字符串"

my_strhash = hashlib.new('sha256')
my_strhash.update(my_str1.encode('utf-8'))
print(f"""
当前加密字符串：{my_str1}
当前加密字符串哈希值：{my_strhash.hexdigest()}
————————————————————""")

my_strhash.update(my_str2.encode('utf-8')) # 或：my_str2.encode()/bytes(my_str2,'utf-8)
print(f"""
当前加密字符串：{my_str1+my_str2}
当前加密字符串哈希值：{my_strhash.hexdigest()}""")

hash1 = hashlib.md5(b'aaa')
hash2 = hashlib.sha1(b'aaa')
hash3 = hashlib.sha256(b'aaa')

print(f"""
md5加密aaa：{hash1.hexdigest()}
sha1加密aaa：{hash2.hexdigest()}
sha256加密aaa：{hash3.hexdigest()}""")