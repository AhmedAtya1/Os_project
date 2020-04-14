from Round import  round
from Process import process

A=process()
B=process()
C=process()
D=process()
E=process()
#p6=process()


A.burst_time=4
B.burst_time=1
C.burst_time=8
D.burst_time=1
E.burst_time=10
#p6.burst_time=3

A.arrival_time=0
B.arrival_time=0
C.arrival_time=0
D.arrival_time=0
E.arrival_time=20
#p6.arrival_time=6


A.name='A'
B.name='B'
C.name='C'
D.name='D'
E.name='E'
#p6.name='p6'

list_p=[A,B,C,D,E]
x=round()
x.quantum=1
x.list_process=list_p
x.calc()
x.out()


