from Scheduler import scheduler
class fcfs (scheduler):
    def calc(self):
        x=[]
        for i in self.list_process:  x.append(i.arrival_time)
        a = zip(x,self.list_process)
        sorted(a)
        b=0
        z=[]
        for j,k in a:
            z[b]=k
            b=b+1
        self.list_element=z