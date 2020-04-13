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

    def out(self):
        for i in self.list_element:
            print(i.p.name + " . start is: " + str(i.start) +" . end is : "+str(i.end))


