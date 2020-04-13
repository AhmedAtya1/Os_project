from Scheduler import scheduler
from Element import element
import operator
class priority(scheduler):
    def calc_non_p(self):
        self.list_process.sort(key=operator.attrgetter('pr'))
        start=0
        for i in range(len(self.list_process)):
            a = element()
            self.list_element.append(a)
            (self.list_element[i]).p = self.list_process[i]
            (self.list_element[i]).start = start
            (self.list_element[i]).end = start + self.list_process.burst_time
           # 555555555555555start = start + self.list_process.burst_time
    def cal_p(self):
        current_list_p=[]
        t = []
        current_p = None
        for q in self.list_process: t.append(q.arrival_time)
        t = list(dict.fromkeys(t))  # remove dub
        t.sort()
        i=0
        x=len(t)
        while i<x :  # this loop iterates on every arrival_time and at the end of each process
            for j in self.list_process:
                if t[i] == j.arrival_time:
                    current_list_p.append(j)
                    current_list_p.sort(key=operator.attrgetter('pr'))
            if current_p is None: # may happen at end of process or at arrival_time
                if len(current_list_p) != 0 :  # because of the last iteration
                    current_p = current_list_p[0]
                    current_element = element()
                    self.list_element.append(current_element)
                    self.list_element[-1].p=current_p
                    self.list_element[-1].start = t[i]
                    if x==i+1:
                        self.list_element[-1].end = t[i] + current_p.burst_time
                        del current_list_p[0]
                        t.append(t[i] + current_p.burst_time)
                        current_p = None
                    else :
                        if t[i] + current_p.burst_time <= t[i + 1]:
                            self.list_element[-1].end = t[i] + current_p.burst_time
                            del current_list_p[0]
                            if t[i] + current_p.burst_time != t[i + 1]: t.insert(i + 1, t[i] + current_p.burst_time)
                            current_p = None
                        elif t[i] + current_p.burst_time > t[i + 1]:
                            current_p.burst_time = current_p.burst_time - (t[i + 1] - t[i])
            else:  # may happen when a process arrive when another process is running
                if current_p.pr <= current_list_p[0].pr :
                    if i==len(t)-1:  # because of the last iteration
                        self.list_element[-1].end = t[i] + current_p.burst_time
                        t.append(t[i] + current_p.burst_time)
                        del current_list_p[0]
                        current_p = None
                    else :
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
                    if i == len(t) - 1:
                        self.list_element[-1].end = t[i] + current_p.burst_time
                        del current_list_p[0]
                        current_p = None
                    else :
                        if t[i] + current_p.burst_time <= t[i + 1]:
                            self.list_element[-1].end = t[i] + current_p.burst_time
                            del current_list_p[0]
                            if t[i] + current_p.burst_time != t[i + 1]: t.insert(i + 1, t[i] + current_p.burst_time)
                            current_p = None
                        elif t[i] + current_p.burst_time > t[i + 1]:
                            current_p.burst_time = current_p.burst_time - (t[i + 1] - t[i])
            x=len(t)
            print(i,x)
            i=i+1
    def calc(self):
        if self.preemptive==0: self.calc_non_p()
        elif self.preemptive==1: self.cal_p()