from Scheduler import scheduler  #????????????
from Element import element
import operator
class round (scheduler):
    quantum=0
    currentTime=0
    currentProcess=''
    queue=[]

    def setQuantum (self):
        self.Sort('burst_time')  # sort processes according to burst time
        self.quantum = (self.list_process[0]).burst_time #Quantum equal shortest burst time by default ?????????
    def calcQuantums(self):
        for i in range(len(self.list_process)): #calculate taken quantums
            (self.list_process[i]).elementsNumber= (self.list_process[i]).burst_time/self.quantum
    def isAllEnded(self):
        for i in range(len(self.list_process)):
            if (self.list_process[i]).state== 'waiting':
                return False
            return True
    def pushIfcamed(self,List_process,Queue,CurrentTime,Quantum):
        self.list_process.sort(reverse=True,key=operator.attrgetter('arrival_time'))
        for i in range(len(List_process)):
            if (List_process[i]).arrival_time in range(CurrentTime-Quantum+1,CurrentTime+1):
                Queue.insert(0,List_process[i])
        self.Sort('arrival_time')





    def calc(self):
        if self.quantum==0 : #not givven
            self.setQuantum()
        self.calcQuantums()
        self.Sort('arrival_time')
        self.currentTime=(self.list_process[0]).arrival_time #begin when first process come
        self.pushIfcamed(self.list_process,self.queue, self.currentTime,1)

        #(self.queue).append(self.list_process[0]) #push first process to queue
        while True:
            if self.isAllEnded():
                break
            if len(self.queue)!=0:
                if (self.queue[0]).elementsNumber>0 and (self.queue[0]).elementsNumber<=1 :
                    a = element()
                    a.p = self.queue[0]
                    a.start = self.currentTime
                    a.end = self.currentTime + int(self.quantum*((self.queue[0]).elementsNumber))
                    a.duration = a.end-a.start
                    (self.list_element).append(a)
                    (self.queue[0]).state='ended'
                    del self.queue[0]
                    self.currentTime +=self.quantum


                elif (self.queue[0]).elementsNumber>1 :
                    a = element()
                    a.p = self.queue[0]
                    a.start = self.currentTime
                    a.end = self.currentTime + self.quantum
                    a.duration = self.quantum
                    (self.list_element).append(a)
                    (self.queue[0]).elementsNumber -=1
                    (self.queue).append(self.queue[0])
                    del self.queue[0]
                    self.currentTime +=self.quantum
                self.pushIfcamed(self.list_process,self.queue,self.currentTime,self.quantum)
            else :
                self.currentTime+=1
                self.pushIfcamed(self.list_process,self.queue,self.currentTime,1)





