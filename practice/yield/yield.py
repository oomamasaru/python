from datetime import datetime
import tracemalloc


def yield_func(n):
    for index in range(n):
        yield index
        index += 1


def return_func(n):
    return_list = []
    for index in range(n):
        return_list.append(index)
    return return_list


tracemalloc.start()

n = 10**7

start_time = datetime.now()
result_list = return_func(n)
for i in result_list:
    pass
print("return_func : ", datetime.now() - start_time)
# start_time = datetime.now()
# iterator = yield_func(n)
# for i in iterator:
#     pass
# print("yield_func : ", datetime.now() - start_time)

ss = tracemalloc.take_snapshot()
for s in ss.statistics("filename"):
    print(s)

tracemalloc.stop()
