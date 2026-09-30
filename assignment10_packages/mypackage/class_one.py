# mypackage/class_one.py  -> module containing ClassOne


class ClassOne:
    def __init__(self, name):
        print("ClassOne constructor called")
        self.name = name

    def greet(self):
        return "Hello from ClassOne, " + self.name
