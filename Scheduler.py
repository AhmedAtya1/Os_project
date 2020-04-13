from Element import element
from Process import process
class scheduler :
    n=0
    list_process=[]
    list_element=[]
    preemptive=0

    def out(self):
        for i in self.list_element:
            print(i.p.name + " . start is: " + str(i.start) +" . end is : "+str(i.end))


