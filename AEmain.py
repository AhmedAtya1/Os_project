from Process import process

p1=process()
p2=process()
p3=process()
p1.burst_time=50
p2=p1
p3=p2
print(p3.burst_time)
p3.burst_time=20
print(p2.burst_time)