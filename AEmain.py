from Process import process
from Priority import  priority
p1=process()
p2=process()
p3=process()
p4=process()
p5=process()
p1.burst_time=4
p2.burst_time=3
p3.burst_time=1
p4.burst_time=5
p5.burst_time=2
p1.arrival_time=0
p2.arrival_time=1
p3.arrival_time=2
p4.arrival_time=3
p5.arrival_time=4
p1.pr=5
p2.pr=3
p3.pr=2
p4.pr=1
p5.pr=1
p1.name='p1'
p2.name='p2'
p3.name='p3'
p4.name='p4'
p5.name='p5'
list_p=[p1,p2,p3,p4,p5]
x=priority()
x.preemptive=1
x.n=5
x.list_process=list_p
x.calc()
x.out()


