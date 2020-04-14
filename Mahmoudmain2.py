from Fcfs import  fcfs
from Process import process

A=process()
B=process()
C=process()
D=process()
E=process()
#F=process()


A.burst_time=5
B.burst_time=3
C.burst_time=1
D.burst_time=2
E.burst_time=3
#F.burst_time=3

A.arrival_time=0
B.arrival_time=1
C.arrival_time=2
D.arrival_time=3
E.arrival_time=4
#F.arrival_time=6


A.name='p1'
B.name='p2'
C.name='p3'
D.name='p4'
E.name='p5'
#F.name='p6'

list_p=[A,B,C,D,E]
x=fcfs()
x.list_process=list_p
x.calc()
x.out()


