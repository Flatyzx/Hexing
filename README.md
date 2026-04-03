# Hexing
> Lately, I’ve been hearing a lot about classes in Python, and honestly, I’ve gotten really excited about developing in Python. So, I created this base class, and I’ll be making more commits to update it.
> As the name suggests, I created a Hexadecimal class that can perform operations, converting from **hex** to **int**, read strings to **hex**, etc.

---

## Initialized
First, you need to import the *Hex* class, which is included in the package files
```pycon
from hexclass import Hex
```
Now you can use it. Here are a few examples

```pycon
h1 = Hex(hexvalue="0x11") # 17
h2 = Hex(integer=32) # 0x20
h3 = Hex() # 0x00, 0
```

## Calling and String
The class can be called or used as a **string**

```pycon
h4 = Hex(integer=255)
h4() #Hex: 0xff, Int: 255
print(h4) #0xff
```

## Sum
One of the methods added is `__add__` and `__radd__`. With both of them together, you can perform any addition, whether it involves **strings**, **integers**, or *hex* values themselves.
```pycon
h5 = h2 + 16 + "0xf" + Hex(integer=1) # 64
print(h5) # 0x40
```

---

## Author
Created by **Flatyzx**