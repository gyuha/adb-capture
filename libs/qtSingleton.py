from PyQt5.QtCore import QObject


class QtSingleton(QObject):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = QObject.__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == "__main__":
    class AA(QtSingleton):
        def __init__(self):
            super().__init__()
            self.num = 123

    aa = AA()
    bb = AA()
    print(aa)
    print(bb)
    print(aa.num)
    print(bb.num)
