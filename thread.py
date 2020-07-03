from threading import Thread,RLock


def my_function1():
    print("123")
    print("456")
    print("789")

def my_function2():
    print("abc")
    print("def")
    print("ghi")

def my_function3():
    print("ABC")
    print("DEF")
    print("GHI")

if __name__ == '__main__':
    lock = RLock()

    def locking_ten(f: callable):
        for i in range(10000):
            with lock:
                f()

    func_list = [my_function1, my_function2, my_function3]
    [Thread(target=locking_ten, args=[func]).start() for func in func_list]
