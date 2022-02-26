import bitcoin.main as btc

bFound = False
for i in range(10000):
    # 개인키 생성
    while(1):
        privKey = btc.random_key()
        dPrivKey = btc.decode_privkey(privKey, 'hex')
        if dPrivKey < btc.N:
            break

    # 개인키로 공개키 생성
    pubKey = btc.privkey_to_pubkey(privKey)

    # 공개키로 지갑 주소 생성 (mainnet 용)
    address = btc.pubkey_to_address(pubKey, 0)

    # 지갑 주소 앞 부분 원하는 문자열인지 확인
    if address[1:4] == 'ABC':
        bFound = True
        break

if bFound:
    # 결과 확인
    print("\n\n개인키 : ", privKey)
    print("\n개인키 --> 공개키 : ", pubKey)
    print("\n공개키 --> 지갑주소 : ", address)
else:
    print("찾지 못했습니다. 다시 시도해 주세요")