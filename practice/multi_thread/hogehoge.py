from concurrent.futures import ThreadPoolExecutor

def func(arg1,arg_dict:dict):
    print(arg1)
    print(arg_dict["num"])
    print(arg_dict["str"])


args_list = [
    {"num" : 1, "str" : "str1"},
    {"num" : 2, "str" : "str2"},
    {"num" : 3, "str" : "str3"}
]
with ThreadPoolExecutor() as executor:
    executor.map(
        func,
        ["引数1","引数2","引数3"],
        [arg for arg in args_list]
    )