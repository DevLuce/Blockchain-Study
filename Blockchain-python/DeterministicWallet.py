import bitcoin.main as btc

# 초기 Seed 값으로 개인키 생성
seed = '초기 seed 값'

# n 개의 개인키 생성
n = 5
error = 0
for i in range(1, (n+1)):
    seed += str(i)
    privKey = btc.sha256(seed)
    dPrivKey = btc.decode_privkey(privKey, 'hex')
    if dPrivKey < btc.N:
        print("개인키 (%d) : %s" % (i, privKey))
    else:
        error += 1

if error > 0:
    print("요청한 seed로 개인키 %d개를 모두 만들지 못함." % n)