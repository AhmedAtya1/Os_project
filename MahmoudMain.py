from Round import  roound
from Process import process

A=process()
B=process()
C=process()
D=process()
#E=process()
#p6=process()


A.burst_time=4.0
B.burst_time=1.0
C.burst_time=8.0
D.burst_time=1.0
#E.burst_time=10
#p6.burst_time=3

A.arrival_time=0.0
B.arrival_time=0.0
C.arrival_time=0.0
D.arrival_time=0.0
#E.arrival_time=20
#p6.arrival_time=6


A.name='A'
B.name='B'
C.name='C'
D.name='D'
#E.name='E'
#p6.name='p6'

list_p=[A,B,C,D]
x=roound()
x.quantum=1.0
x.list_process=list_p
x.real()
x.calc()
print(x.waiting_time())
x.empty()
x.out()


