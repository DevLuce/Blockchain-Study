import hashlib
import binascii

privKey = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'

# Base58 Encoding
s = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# version prefix를 추가. 0x80 ~ Private key WIF
# 공개키를 compressed form으로 사용할 때는 이 뒤에 '01'을 추가
prefixPayload = '80' + privKey

# Checksum을 구함. version + payload에 double-SHA256을 수행하고
# 앞 부분의 4바이트를 prefixPayload 뒤에 추가
versionPayload = binascii.unhexlify(prefixPayload)
h = hashlib.sha256(hashlib.sha256(versionPayload).digest()).digest()
h = ''.join('{:02x}'.format(y) for y in h)
versionPayloadChecksum = prefixPayload + h[0:8]

# Base58Check encoding을 수행
eKey = int(versionPayloadChecksum, 16)
base58 = ''
while(1):
    m, r = divmod(eKey, 58)
    base58 += s[r]
    if m == 0:
        break
    eKey = m

wif = base58[::-1]
print("\n개인기 (Hex): ", privKey.lower())
print("개인기 (WIF): ", wif)