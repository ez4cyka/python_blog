import bcrypt

#加密保存用户密码
salt  = bcrypt.gensalt()
print(salt.decode('utf-8'))
pwd = '123456'
hashed = bcrypt.hashpw(pwd.encode(),salt)
print(hashed.decode('utf-8'))






