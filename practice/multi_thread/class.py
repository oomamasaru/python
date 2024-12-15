class hoge() :
    def __init__(self) :
        self.hoge = "hoge"
    
    def func(self) :
        self.func2(self.hoge)
        
    def func2(self,hoge) :
        self.hoge = "hogehoge"
        print(hoge)

hooge = hoge()
hooge.func()