from Element import element
from Process import process
import operator

class scheduler :
    n=0
    list_process=[]
    list_element=[]
    preemptive=0
    def Sort(self,sort_according_to_what='burst_time'):
        self.list_process.sort(key=operator.attrgetter(sort_according_to_what))

    def put_element(self,process,start,end):
       a=element()
       self.list_element.append(a)
       (self.list_element[-1]).p =process
       (self.list_element[-1]).start=start
       (self.list_element[-1]).end = end
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


