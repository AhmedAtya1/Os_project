from Scheduler import scheduler
from Element import element
from copy import deepcopy
import operator
class priority(scheduler):
    queue = []
    currentTime = 0
    def pushIfcamed(self,Queue, Start, End):
        for i in range(len(self.list_process)):
            if (self.list_process[i]).arrival_time in range(Start, End):
                Queue.append(self.list_process[i])
        Queue.sort(key=operator.attrgetter('pr'))

    def addElement(self, start, proc):
       a = element()
       a.start = start
       a.end = proc.burst_time + start
       a.p = proc
       a.duration = a.start - a.end
       self.list_element.append(a)



    def calc_non_p(self):
        self.int_le3yon_a7md_m7mod()
        self.Sort('arrival_time')
        self.currentTime= (self.list_process[0]).arrival_time
        self.pushIfcamed(self.queue,self.currentTime,self.currentTime+1)
        for i in range(len(self.list_process)):
            if len(self.queue)!=0:
                self.addElement(self.currentTime,self.queue[0])
                oldCur=self.currentTime
                self.currentTime += self.queue[0].burst_time
                del self.queue[0]
                self.pushIfcamed(self.queue, oldCur+1, self.currentTime + 1)
            else:
                for i in range(len(self.list_process)):
                    if (self.list_process[i]).arrival_time > self.currentTime:
                        self.currentTime=self.list_process[i].arrival_time
                        break
                self.pushIfcamed(self.queue, self.currentTime, self.currentTime + 1)
                self.addElement(self.currentTime,self.queue[0])
                self.currentTime += self.queue[0].burst_time
                ooldCur = self.currentTime
                del self.queue[0]
                self.pushIfcamed(self.queue, ooldCur+1, self.currentTime + 1)



    def cal_p(self):
        current_list_p=[]
        t = [] #time
        current_p = None
        for q in self.list_process: t.append(q.arrival_time)
        t = list(dict.fromkeys(t))  # remove dub
        t.sort()
        i=0
        x=len(t)
        while i<x :  # this loop iterates on every arrival_time and at the end of each process
            for j in self.list_process:     # 7ad geh  ?
                if t[i] == j.arrival_time:
                    current_list_p.append(j)     # tab t3ala ya m3lm
                    current_list_p.sort(key=operator.attrgetter('pr'))
            if current_p is None: # may happen at end of process or at arrival_time
                if len(current_list_p) != 0 :  # because of the last iteration
                    current_p = current_list_p[0]
                    current_element = element()
                    self.list_element.append(current_element)
                    self.list_element[-1].p=current_p
                    self.list_element[-1].start = t[i]
                    if x==i+1:  # because of the last iteration
                        self.list_element[-1].end = t[i] + current_p.burst_time
                        del current_list_p[0]
                        t.append(t[i] + current_p.burst_time)
                        current_p = None
                    else :  # da l 3ady
                        if t[i] + current_p.burst_time <= t[i + 1]:
                            self.list_element[-1].end = t[i] + current_p.burst_time
                            del current_list_p[0]
                            if t[i] + current_p.burst_time != t[i + 1]: t.insert(i + 1, t[i] + current_p.burst_time)
                            current_p = None
                        elif t[i] + current_p.burst_time > t[i + 1]:
                            current_p.burst_time = current_p.burst_time - (t[i + 1] - t[i])
            else:  # may happen when a process arrive when another process is running
                if current_p.pr <= current_list_p[0].pr:
                    if i==len(t)-1:  # because of the last iteration
                        self.list_element[-1].end = t[i] + current_p.burst_time
                        t.append(t[i] + current_p.burst_time)
                        del current_list_p[0]
                        current_p = None
                    else :  # da l 3ady
                        if t[i] + current_p.burst_time <= t[i + 1]:
                            self.list_element[-1].end = t[i] + current_p.burst_time
                            del current_list_p[0]
                            if t[i] + current_p.burst_time != t[i + 1]: t.insert(i + 1, t[i] + current_p.burst_time)
                            current_p = None
                        elif t[i] + current_p.burst_time > t[i + 1]:
                            current_p.burst_time = current_p.burst_time - (t[i + 1] - t[i])
                else :
                    self.list_element[-1].end = t[i]
                    current_p = current_list_p[0]
                    current_element = element()
                    self.list_element.append(current_element)
                    self.list_element[-1].p = current_p
                    self.list_element[-1].start = t[i]
                    if i == len(t) - 1:  # because of the last iteration
                        self.list_element[-1].end = t[i] + current_p.burst_time
                        t.append(t[i] + current_p.burst_time)
                        del current_list_p[0]
                        current_p = None
                    else : # da l 3ady
                        if t[i] + current_p.burst_time <= t[i + 1]:
                            self.list_element[-1].end = t[i] + current_p.burst_time
                            del current_list_p[0]
                            if t[i] + current_p.burst_time != t[i + 1]: t.insert(i + 1, t[i] + current_p.burst_time)
                            current_p = None
                        elif t[i] + current_p.burst_time > t[i + 1]:
                            current_p.burst_time = current_p.burst_time - (t[i + 1] - t[i])
            x=len(t)
            i=i+1
    def calc(self):
        if self.preemptive==0: self.calc_non_p()
        elif self.preemptive==1: self.cal_p()