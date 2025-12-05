import hashlib

def gen_md5(input: str):
    encryptor = hashlib.md5()
    encryptor.update(input.encode('utf-8'))
    return encryptor.hexdigest()

i = 1
code = "yzbqklnj"
while True:
    ans = gen_md5(code + str(i))
    if ans[:5] == "00000":
        print(i)
        print(ans)
        break
    i += 1
