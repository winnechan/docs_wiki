from .a import A

class B(A):
    def __init__(self, name, salary):
        super(B, self).__init__(name, salary)

    def _local_func(self, x: int):
        return "test func"