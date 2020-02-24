class Person:
    def __init__(self,content):
        self.content = content

    def cap(self):
        return self.content[0].upper() + self.content[1:]

x = Person("hehe")
print(x.cap())