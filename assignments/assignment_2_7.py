class ReadOnly:
    def __init__(self):
        self._value = 42

    @property
    def value(self):
        return self._value

r = ReadOnly()
print(r.value)  # 42
# r.value = 99  # Error: AttributeError
