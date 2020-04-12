from SJF import Sjf
from Fcfs import fcfs
from Process import process
import random

test=Sjf()
pro=[]


for i in range (10):
    a=process()
    pro.append(a)
    pro[i].name='p'+str(i)
    pro[i].burst_time=random.randint(1,100)
test.list_process=pro
test.calc()
for i in range(10):

    print((test.list_element[i]).p)




