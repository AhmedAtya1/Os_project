from Scheduler import scheduler
from Element import element


class fcfs (scheduler):
    def calc(self):
        x=[]
        for i in self.list_process:  x.append(i.arrival_time)
        a = zip(x,self.list_process)
        sorted(a)
        b=0
        for j,k in a:
            self.list_process[b]=k
            b=b+1
        for i in range(len(self.list_process)):
            self.list_element[i] = element()
            (self.list_element[i]).p = self.list_process[i]