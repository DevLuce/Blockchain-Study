import bitcoin.main as btc

# 특정 문자열로 256-bit 개인키 생성(long brain wallet passphrase)
passphrase = 'Brain Wallet 시험용 개인키'
privKey = btc.sha256(passphrase)
dPrivKey = btc.decode_privkey(privKey, 'hex')
if dPrivKey < btc.N: # secp256k1의 N보다 작으면 OK
    # 개인키로 공개키 생성
    pubKey = btc.privkey_to_pubkey(privKey)

    # 공개키로 지갑 주소 생성 (mainnet용)
    address = btc.pubkey_to_address(pubKey, 0)

    # 결과 확인
    print("\n\nPassphrase : ", passphrase)
    print("\n개인키 : ", privKey)
    print("개인키 --> 공개키 : ", pubKey)
    print("\n공개키 --> 지갑주소 : ", address)
else:
    print("다른 Passphrase로 다시 시도해주세요.")