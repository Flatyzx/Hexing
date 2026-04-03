from __future__ import annotations
from functools import wraps
import errs as err

hexDictValues: dict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, 
                        "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13,
                        "e":14, "f":15}

class hutils:
    @staticmethod
    def read_hex(_hxvv: str) -> int:
        if not isinstance(_hxvv, str): raise err.IsNotString(_hxvv)

        hxv = _hxvv.lower()
        result = 0

        if hxv[:2] != "0x": raise err.IsNotHex(hxv)
        if hxv[2:] == "": raise err.HexIncompleted(hxv)

        hx_inv = hxv[::-1]
        mul = 1
        for i in range(len(hx_inv)-2): #-2 é por causa de 0x
            c = hx_inv[i]
            if not c in hexDictValues.keys(): raise err.IsNotHex(hxv)

            result += hexDictValues[c] * mul
            mul *= 16
        
        return result, hxv

    @staticmethod
    def ishex(vv) -> bool:
        try: result, _ = hutils.read_hex(vv)
        except (err.IsNotString, err.IsNotHex, err.HexIncompleted) as e:
            return False 
        return True
    
    @staticmethod
    def positiveInt(func):
        @wraps(func)
        def wrapper(other: int):
            if other < 0: raise err.NegativeInteger(other)
            return func(other)
        return wrapper
    
    @staticmethod
    def Hexing(func):
        @wraps(func)
        def wrapper(other: str):
            if not hutils.ishex(other): raise err.IsNotHex(other)
            return func(other)
        return wrapper

    def __new__(cls): raise err.InstantiableClass(cls)

class Hex:
    def __init__(self, hexvalue: str="0x00", integer: int=0):
        if not isinstance(integer, int): raise err.IsNotInteger(integer)

        try: result, _ = hutils.read_hex(hexvalue)
        except (err.IsNotString ,err.IsNotHex, err.HexIncompleted) as e: raise e
        
        self.__hexv = hexvalue if hexvalue != "0x00" else hex(integer)
        self.__integerv = result if result != 0 else integer
    
    @property
    def hexv(self) -> str: return self.__hexv
    @hexv.setter
    def hexv(self, hx) -> None:
        if not hutils.ishex(hx): raise err.IsNotHex(hx)
        self.__hexv = hx
        self.__integerv, _= hutils.read_hex(hx)

    @property
    def integerv(self) -> int: return self.__integerv
    @integerv.setter
    def integerv(self, n: int) -> None:
        if n < 0: raise err.NegativeHex(n)
        self.__integerv = n
        self.__hexv = hex(n)

    def __str__(self) -> str: return self.__hexv
    def __call__(self, *args) -> None: 
        print(f"Hex: {self.__hexv}, Int: {self.integerv}")
        
    
    def __add__(self, other: int | str | Hex) -> Hex:
        @hutils.positiveInt
        def __isInteger(other: int): 
            result = self.__integerv + other
            return Hex(integer=result)
        
        @hutils.Hexing
        def __isString(other: str): 
            integer, _ = hutils.read_hex(other)
            result = integer + self.__integerv
            return Hex(integer=result)
    
        def __isHex(other: Hex): 
            result = self.__integerv + other.__integerv
            return Hex(integer=result)

        if isinstance(other, int):  return __isInteger(other)
        elif isinstance(other, str): return __isString(other)
        elif isinstance(other, Hex): return __isHex(other)
        else: raise er.UnknownType(other)
    
    def __radd__(self, other):
        return self.__add__(other)