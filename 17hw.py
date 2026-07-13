class MetaC(type):
    def __new__(mcls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value):
                if key[0] != "_":
                    raise ValueError("Method is public")
        return super().__new__(mcls, name, bases, attrs)
    

class Test(metaclass=MetaC):

    def _one(self):
        pass

    def _two(self):
        pass

    def three(self):
        pass

    def _four(self):
        pass


t = Test()