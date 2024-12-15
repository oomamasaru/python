from concurrent.futures import ThreadPoolExecutor

def func(*args,**kwargs) :
    print(args)
    print(kwargs)

# def func(**args) :
#     print(args[0])
#     print(args[1])

# executer = ThreadPoolExecutor(max_workers=1)

apple = "apple"
orange = "orange"

func((apple),{orange:orange})
# executer.map(
#     func,
#     [{index:index,apple:apple} for index in range(0,5)]

# )