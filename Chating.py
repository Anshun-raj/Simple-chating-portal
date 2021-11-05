from threading import *
from time import sleep
class p1(Thread):
    def run(self):
        for i in range(100):
            n=input("Anshu's Turn:")
            sleep(20)


class p2(Thread):
    def run(self):
        for i in range(100):
            n=input("Rohit's Turn:")
            sleep(20)


t1=p1()
t2=p2()
t1.start()
sleep(10)
t2.start()
