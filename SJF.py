from Scheduler import scheduler
from Element import element
from copy import deepcopy
import operator

class Sjf(scheduler):
    according_to_arrival=[]
    def p_sort_arrival(self):
        self.according_to_arrival=deepcopy(self.list_process)
        self.according_to_arrival.sort(key=operator.attrgetter('arrival_time'))

    def p_sort(self):
        self.list_process.sort(key=operator.attrgetter('burst_time'))
    def put_element(self,process,start,end,duration):
        a=element()
        self.list_element.append(a)
        (self.list_element[-1]).p =process
        (self.list_element[-1]).start=start
        (self.list_element[-1]).end = end
        (self.list_element[-1]).duration = duration
    def calc(self):
        self.p_sort()
        self.p_sort_arrival()
        if self.preemptive==0:
            for i in range(len(self.list_process)):
                a=element()
                self.list_element.append(a)
                (self.list_element[i]).p=self.list_process[i]
        else:
            check=0
            while len(self.according_to_arrival)!=check:
                a = element()
                for i in range(len(self.according_to_arrival)):
                    temp=self.according_to_arrival
                    if temp[i].burst_time==0:continue
                    if i!=len(temp)-1:
                        Du=temp[i+1].arrival_time-temp[i].arrival_time
                        if Du>=temp[i].burst_time:
                            self.list_element.append(a)
                            (self.list_element[i]).p = self.according_to_arrival[i]
                            (self.list_element[i]).start = temp[i].arrival_time
                            (self.list_element[i]).end = temp[i].arrival_time+temp[i].burst_time
                            (self.list_element[i]).duration = temp[i].burst_time
                            temp[i].burst_time = 0
                            check += 1
                        else:
                            if (temp[i+1].burst_time < temp[i].burst_time)and(temp[i+1].burst_time!=0):
                                self.put_element(temp[i], temp[i].arrival_time, temp[i+1].arrival_time, Du)
                                temp[i].burst_time -= Du
                            else:
                                for j in range(len(self.according_to_arrival))[i+1:]:
                                    DURA=temp[j+1].arrival_time-temp[i].arrival_time
                                    if DURA>=temp[i].burst_time:
                                        self.put_element(temp[i], temp[i].arrival_time, temp[i].arrival_time+temp[i].burst_time, temp[i].burst_time)
                                        temp[i].burst_time = 0
                                        check += 1
                                        break
                                    else:
                                        myReminder_dur = temp[i].burst_time-DURA
                                        if (myReminder_dur>temp[j+1].burst_time)and(temp[j+1].burst_time!=0):
                                            self.put_element(temp[i], temp[i].arrival_time, temp[i].arrival_time+DURA, temp[i].burst_time)
                                            temp[i].burst_time -= DURA
                                self.put_element(temp[i], temp[i].arrival_time, temp[i].arrival_time+temp[i].burst_time,temp[i].burst_time )
                                temp[i].burst_time = 0
                                check += 1
                    else:
                        if (temp[i]<=temp[0].burst_time)or(temp[0].burst_time == 0):
                            self.put_element(temp[i], temp[i].arrival_time, temp[i].arrival_time + temp[i].burst_time,
                                             temp[i].burst_time)
                            temp[i].burst_time = 0
                            check += 1
