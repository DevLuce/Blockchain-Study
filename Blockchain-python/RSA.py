# Public Key(RSA)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Private Key와 Public Key 쌍 생성
# Private Key는 소유자가 보관, Public Key는 공개
keyPair = RSA.generate(2048)
privKey = keyPair.exportKey()
pubKey = keyPair.publickey()

# keyPair의 p,q,e,d 확인
keyObj = RSA.importKey(privKey)
print("p = ", keyObj.p)
print("q = ", keyObj.q)
print("e = ", keyObj.e)
print("d = ", keyObj.d)

# 암호화할 원문
plainText = 'This is Plain text. It will be encrypted using RSA.'
print()
print("원문 :")
print(plainText)

# 공개키로 원문 암호화
encryptor = PKCS1_OAEP.new(keyPair)
cipherText = encryptor.encrypt(plainText.encode())
print("\n")
print("암호문 :")
print(cipherText.hex())

# Private key를 소유한 수신자는 자신의 Private key로 암호문을 해독
# pubKey와 쌍을 이루는 privKey만이 이 암호문을 해독
# key = RSA.importKey(privKey)
decryptor = PKCS1_OAEP.new(keyPair)
plainText2 = decryptor.decrypt(cipherText)
plainText2 = plainText2.decode()
print("\n")
print("해독문 :")
print(plainText2)