import datetime

class Hoge:
    # @staticmethod
    def time_measurement(func):
        def execute(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            print("実行時間：" + str(datetime.datetime.now() - start_time))
            return result
        return execute

    @time_measurement
    def print_hoge(self):
        print("hogehoge")

if __name__ == "__main__":
    hoge = Hoge()
    hoge.print_hoge()
