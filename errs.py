class IsNotInteger(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThe value '{self.value}' is not int OR is str\033[m")

class IsNotHex(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThe value '{self.value}' is not hex\033[m")

class IsNotString(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThe value '{self.value}' is not str\033[m")

class HexIncompleted(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThe Hex '{self.value}' is missing the hex value\033[m")

class NegativeHex(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThe Hex '{self.value}' should be positive\033[m")

class NegativeInteger(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThe Integer '{self.value}' should be positive\033[m")

class UnknownType(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThis class is unknown ({self.value})\033[m")

class InstantiableClass(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"\033[31mThe class '{self.value}' can't be initialized")