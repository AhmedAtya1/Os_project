from Process import process
from Priority import  priority
p1=process()
p2=process()
p3=process()
p4=process()
p5=process()
#p6=process()
#p7=process()
p1.burst_time=4
p2.burst_time=10
p3.burst_time=2
p4.burst_time=20
p5.burst_time=2
#p6.burst_time=15
#7.burst_time=8
p1.arrival_time=0
p2.arrival_time=2
p3.arrival_time=4
p4.arrival_time=6
p5.arrival_time=8
#p6.arrival_time=5
#p7.arrival_time=15
p1.pr=4
p2.pr=2
p3.pr=1
p4.pr=3
p5.pr=5
#p6.pr=10
#p7.pr=9
p1.name='p1'
p2.name='p2'
p3.name='p3'
p4.name='p4'
p5.name='p5'
#p6.name='p6'
#p7.name='p7'
list_p=[p1,p2,p3,p4,p5]
x=priority()
x.preemptive=1
x.n=5
x.list_process=list_p
x.calc()
x.out()


