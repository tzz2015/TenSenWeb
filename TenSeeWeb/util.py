import hashlib


# 生成MD5字符串
def md5_str(s):
    hl = hashlib.md5()
    hl.update(s.encode("utf-8"))
    return hl.hexdigest()
