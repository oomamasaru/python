from concurrent.futures import ThreadPoolExecutor
import time

def print_every_two_sec(num:int) -> str :
    """2秒ごとにコンソール出力を行う。

    Args:
        num (int): 出力回数

    Returns:
        str: 完了メッセージ
    """
    for cnt in range(num) :
        time.sleep(2)
        print(f"print_every_two_sec  {cnt+1}回目")
    return f"print_every_two_sec {num}回実行完了"

def print_every_three_sec(num:int) -> str :
    """3秒ごとにコンソール出力を行う。

    Args:
        num (int): 出力回数

    Returns:
        str: 完了メッセージ
    """
    for cnt in range(num) :
        time.sleep(3)
        print(f"print_every_three_sec  {cnt+1}回目")
    return f"print_every_three_sec {num}回実行完了"

if __name__ == "__main__" :
    print("開始")
    with ThreadPoolExecutor(max_workers=3) as executor :
        func1_result = executor.submit(print_every_two_sec,3)
        print(func1_result.running())
        print(func1_result.done())
        func1_result.cancelled()
        print(func1_result.running())
        print(func1_result.done())

    print(func1_result.result())

    print("終了")