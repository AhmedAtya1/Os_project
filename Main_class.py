from SJF import Sjf
from Fcfs import fcfs
from Process import process
import random

test=Sjf()
pro=[]


for i in range (4):
    a=process()
    pro.append(a)
    pro[i].name='p'+str(i)
pro[0].burst_time,pro[1].burst_time,pro[2].burst_time,pro[3].burst_time=8,4,9,5
pro[0].arrival_time,pro[1].arrival_time,pro[2].arrival_time,pro[3].arrival_time=0,1,2,3
test.preemptive=1
test.list_process=pro
test.calc()
for i in range(len(test.list_element)):

    print(test.list_element[i])
#,pro[4].burst_time,pro[5].burst_time
#,pro[4].arrival_time,pro[5].arrival_time