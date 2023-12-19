class A:
    def __init__(self):
        return
    def create(self):
        self.x *= 2
class B(A):
    x = 2
a = B()
a.create()
print(a.x)
        