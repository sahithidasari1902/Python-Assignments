# mypackage/class_two.py  -> module containing ClassTwo

# Q7. Relative import: '.' means "the same package as this file"
from .class_one import ClassOne


class ClassTwo:
    def __init__(self, a, b):
        print("ClassTwo constructor called")
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def use_class_one(self):
        # ClassTwo uses ClassOne, imported with a relative import above
        helper = ClassOne("called from ClassTwo")
        return helper.greet()
