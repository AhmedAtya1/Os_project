from Element import element
from copy import deepcopy
import operator

class scheduler :
    n=0
    unmodified=[]
    list_process=[]
    list_element=[]
    preemptive=0
    def real(self):
        self.unmodified = deepcopy(self.list_process)
    def Sort(self,sort_according_to_what='burst_time'):
        self.list_process.sort(key=operator.attrgetter(sort_according_to_what))
    def waiting_time(self):
        if len(self.list_element)!=0:
            time = []
            final=0.0
            for i in self.unmodified:
                new=[]
                for j in self.list_element:
                    if j.p.name==i.name:
                        new.append(j)
                if len(new)!=0:
                    if len(new)==1:
                        t=new[0].start-i.arrival_time
                    else:
                        t = new[-1].end-new[0].start-i.burst_time + new[0].start  - i.arrival_time
                    time.append(t)
            for k in time :
                final += float(k)
            final /=  len(self.list_process)
            return final

    def int_le3yon_a7md_m7mod(self):
        for i in self.list_process:
            i.burst_time=round(i.burst_time)
            i.arrival_time=round(i.arrival_time)



    def empty(self):
        if len(self.list_element)!=0:
            for i in range(len(self.list_element)) :
                if self.list_element[i] != self.list_element[-1]:
                    if self.list_element[i].end != self.list_element[i+1].start:
                        a = element()
                        a.p.name='empty'
                        a.start=self.list_element[i].end
                        a.end=self.list_element[i+1].start
                        self.list_element.insert(i+1,a)


    def out(self):
        for i in self.list_element:
            print(i.p.name + " . start is: " + str(i.start) +" . end is : "+str(i.end))





