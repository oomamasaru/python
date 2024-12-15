from concurrent.futures import ThreadPoolExecutor

def decorator(fn,*args, **kwargs):
    """関数実行前後に開始宣言・終了宣言を行うデコレータ

    Args:
        fn (function): 実行したい関数
        *args: 実行したい関数に渡す引数
    """
    print(f"【{fn.__name__}】 start")
    # 関数を実行
    fn(*args, **kwargs)
    print(f"【{fn.__name__}】 end\n")

def func1(arg1):
    print("func1_arg1   :",type(arg1),arg1)

def func2(arg1,arg2):
    print("func2_arg1   :",type(arg1),arg1)
    print("func2_arg2   :",type(arg2),arg2)

def func3(arg1,arg2="default 3-2",arg3="default 3-3"):
    print("func3_arg1   :",type(arg1),arg1)
    print("func3_arg2   :",type(arg2),arg2)
    print("func3_arg3   :",type(arg3),arg3)

# デコレータ呼び出し
decorator(func1,"1-1")
decorator(func2,"2-1","2-2")
decorator(func3,"3-1",arg3="3-3")


# def func(args:tuple):
#     print("args   :",type(args),args)
#     print("")

# func(("1-1"))
# func(("2-1","2-2"))
# func(("3-1","3-2","3-3"))


# def func(*args,**kwargs):
#     print("args   :",type(args),args)
#     print("kwargs :",type(kwargs),kwargs)

# func("引数1","引数2",arg3="引数3",arg4="引数4")

# hoge = (1,10)
# hogehoge = {"hoge":"hoge1","hogehoge":"hogehoge1"}
# print(hoge)
# print(*hoge)
# print(hogehoge)
# print(type(**hogehoge))

# l = [1, 2, 3, 4, 5]

# a, b, *_ = l
# print(type(a),a)
# print(type(b),b)
# print(type(_),_)