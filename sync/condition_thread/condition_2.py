import threading
import time
from threading import Condition


# 条件变量  用于复杂的线程同步
# 当前无法实现交互 怎么实现呢 引入condition

class Consume(threading.Thread):
    def __init__(self, condition: Condition):
        super().__init__(name='consume')
        self.condition = condition

    def run(self):
        with self.condition:
            for i in range(10):
                # 要先调用with  分配锁和释放锁
                self.condition.wait()
                print(threading.current_thread().name, " 消费:", i)
                time.sleep(1)
                self.condition.notify()


class Product(threading.Thread):
    def __init__(self, condition: Condition):
        super().__init__(name='Product')
        self.condition = condition

    def run(self):
        with self.condition:
            for j in range(10):
                print(threading.current_thread().name, "生产:", j)
                time.sleep(1)
                self.condition.notify()
                self.condition.wait()


if __name__ == '__main__':
    locks = Condition()
    c = Consume(locks)
    p = Product(locks)
    # 启动顺序，要先wait  再去notify
    c.start()
    p.start()

    c.join()
    p.join()
