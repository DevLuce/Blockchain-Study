from Crypto.Hash import MD5, RIPEMD, SHA, SHA256

msg = "이 문서의 Hash Value?"
print("\nMessage : ", msg)

msg = msg.encode()

# MD5
h = MD5.new()
h.update(msg)
hv = h.hexdigest()
print("\nMD5 (%d bit) : %s" % (len(hv) * 4, hv))

# RIPEMD160
h = RIPEMD.new()
h.update(msg)
hv = h.hexdigest()
print("RIPMED (%d bit) : %s" % (len(hv) * 4, hv))

# SHA
h = SHA.new()
h.update(msg)
hv = h.hexdigest()
print("SHA (%d bit) : %s" % (len(hv) * 4, hv))

# SHA256
h = SHA256.new()
h.update(msg)
hv = h.hexdigest()
print("SHA256 (%d bit) : %s" % (len(hv) * 4, hv))

# Double-SHA256
h1 = SHA256.new()
h1.update(msg) # 1st SHA256

h2 = SHA256.new()
h2.update((h1.hexdigest()).encode())

hv = h2.hexdigest()
print("Double-SHA256 (%d bit) : %s" % (len(hv) * 4, hv))