class Hoge():
    def __init__(self):
        print(1)

    def __enter__(self):
        print(2)
        return self

    def execute(self):
        print(4)
        print("hoge")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type : ", exc_type)
        print("exc_val  : ", exc_val)
        print("exc_tb   : ")
        import traceback
        traceback.print_tb(exc_tb)
        return True


with Hoge() as hoge:
    print(3)
    raise TypeError("HogeによるTypeErrorが発生しました")
    hoge.execute()
    print(5)
print(7)
