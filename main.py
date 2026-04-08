from hexclass import Hex

h1 = Hex(hexvalue="0x11") # 17
h2 = Hex(integer=32) # 0x20
h3 = Hex() # 0x00, 0


h4 = Hex(integer=255)
h4() #Hex: 0xff, Int: 255
print(h4) #0xff


h5 = h2 + 16 + "0xf" + Hex(integer=1)# 64
print(h5) # 0x40

h6 = 34 - h2 - "0x1" - Hex(integer=1) # 0
print(h6) # 0x0

h1 += "0x9" + Hex(hexvalue="0x6") # 32
print(h1) # 0x20

h2 -= "0x10" - Hex(integer=4) # 20
print(h2) # 0x14