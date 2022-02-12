# Advanced Encryption Standard(AES)
# CBC(Cipher Block Chain) 모드로 암호화
from Crypto.Cipher import AES
from Crypto import Random
import numpy as np

secretKey128 = b'0123456701234567'
secretKey192 = b'012345670123456701234567'
secretKey256 = b'0123456701234567012345670123456701234567'

# 128-bit key
secretKey = secretKey128
plainText = 'This is Plain Text. It will be encrypted using AES with CBC mode.'
print("\n\n")
print("원문 :")
print(plainText)

# CBC 모드에서는 plain text가 128-bit(16byte)의 배수가 돼야 하므로 padding 필요
# padding으로 NULL 문자 삽임. 수신자는 별도로 padding 제거할 필요 없음.
n = len(plainText)
if (n%16) != 0:
    n = n + 16 - (n % 16)
    plainText = plainText.ljust(n, '\0')

# initialization vector. iv도 수신자에서 송신
iv = Random.new().read(AES.block_size)
# ivcopy = np.copy(iv) # 수신자에게 보낼 복사본
ivcopy = iv

# 송신자는 secretKey와 iv로 plainText를 암호문으로 변환
aes = AES.new(secretKey, AES.MODE_CBC, iv)
cipherText = aes.encrypt(str.encode(plainText))
print("\n\n\n")
print("암호문 :")
print(cipherText.hex())

# 암호문, secretKey, ivcopy를 수신자에게 보내면 수신자는 암호문을 해독할 수 있음
aes = AES.new(secretKey, AES.MODE_CBC, ivcopy)
plainText2 = aes.decrypt(cipherText)
plainText2 = plainText2.decode()
print("\n\n\n")
print("해독문 :")
print(plainText2)