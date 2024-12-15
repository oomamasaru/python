from concurrent.futures import ThreadPoolExecutor
import time

def print_func(args) :
    id = args[0]
    num = args[1]
    for cnt in range(num) :
        time.sleep(3)
        print(f"{id} : {cnt+1}回目")
    return f"{id} {num}回実行完了"
def func() :
    with ThreadPoolExecutor(max_workers=1) as executor :
        executor.submit(main)
def main() :
    with ThreadPoolExecutor(max_workers=4) as executor:
        func_results = executor.map(print_func,[
            ("A",5),
            ("B",4),
            ("C",3),
            ("D",2),
        ])

    print(list(func_results))

if __name__ == "__main__" :
    func()