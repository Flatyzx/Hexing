# Hexing
> Lately, I’ve been hearing a lot about classes in Python, and honestly, I’ve gotten really excited about developing in Python. So, I created this base class, and I’ll be making more commits to update it.
> As the name suggests, I created a Hexadecimal class that can perform operations, converting from **hex** to **int**, read strings to **hex**, etc.

---

## Initialized
First, you need to import the *Hex* class, which is included in the package files
```python
from hexclass import Hex
```
Now you can use it. Here are a few examples

```python
h1 = Hex(hexvalue="0x11") # 17
h2 = Hex(integer=32) # 0x20
h3 = Hex() # 0x00, 0
```

## Calling and String
The class can be called or used as a **string**

```python
h4 = Hex(integer=255)
h4() #Hex: 0xff, Int: 255
print(h4) #0xff
```

## Sum
One of the methods added is `__add__` and `__radd__`. With both of them together, you can perform any addition, whether it involves **strings**, **integers**, or *hex* values themselves.
```python
h5 = h2 + 16 + "0xf" + Hex(integer=1) # 64
print(h5) # 0x40
```

## Sub
The `__sub__` method has the same properties as `__add__`, with a few differences: the result cannot be negative.
```python
h6 = 34 - h2 - "0x1" - Hex(integer=1) # 0
print(h6) # 0x0
```

## Self-Increase and Decrease
To add to the class itself, you can use the `__iadd__` or `__isub__` methods. Or, in simpler terms: (**+=** or **-=**).
```python
h1 += "0x9" + Hex(hexvalue="0x6") # 32
print(h1) # 0x20

h2 -= "0x10" - Hex(integer=4) # 20
print(h2) # 0x14
```
**IMPORTANT**: Remember that in subtraction, the order of the terms matters a lot and can lead to an unexpected result. So, **Be careful!**

---

## Author
Created by **Flatyzx**