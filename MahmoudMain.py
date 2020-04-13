from Round import  round
from Process import process

p1=process()
p2=process()
p3=process()
p1.burst_time=24
p2.burst_time=3
p3.burst_time=3
p1.arrival_time=0
p2.arrival_time=1
p3.arrival_time=2
p1.name='p1'
p2.name='p2'
p3.name='p3'
list_p=[p1,p2,p3]
x=round()
x.quantum=4
x.list_process=list_p
x.calc()
x.out()


