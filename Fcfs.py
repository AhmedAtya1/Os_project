from Scheduler import scheduler
from Element import element
import operator
class fcfs (scheduler):
    currentTime = 0


    def addElement(self,start,proc):
        a = element()
        a.start=start
        a.end=proc.burst_time+start
        a.p=proc
        a.duration=a.start-a.end
        self.list_element.append(a)
        self.currentTime =a.end
    def calc(self):
        self.int_le3yon_a7md_m7mod()
        self.list_process.sort(key=operator.attrgetter('arrival_time'))
        for i in range(len(self.list_process)):
            if (self.list_process[i]).arrival_time>self.currentTime:
                self.addElement((self.list_process[i]).arrival_time,self.list_process[i])
            else :
                self.addElement(self.currentTime, self.list_process[i])