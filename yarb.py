from Scheduler import scheduler
from Element import element
from copy import deepcopy


class Sjf(scheduler):
    according_to_arrival=[]
    def begin(self):
        self.Sort('arrival_time')
        self.according_to_arrival= deepcopy(self.list_process)
        self.Sort()
    def put_element(self,process,start,end,duration):
        a=element()
        self.list_element.append(a)
        (self.list_element[-1]).p =process
        (self.list_element[-1]).start=start
        (self.list_element[-1]).end = end
        (self.list_element[-1]).duration = duration
    def calc(self):
        self.begin()
        if self.preemptive==0:
            for i in range(len(self.list_process)):
                a=element()
                self.list_element.append(a)
                (self.list_element[i]).p=self.list_process[i]
        else:
            print('h')
