from Scheduler import scheduler
from Element import element
from copy import deepcopy
from Process import process


class Sjf(scheduler):
    according_to_arrival=[]
    def begin(self):
        self.Sort('arrival_time')
        self.according_to_arrival= deepcopy(self.list_process)
        self.Sort()
    def put_element(self,process,start,end):
        a=element()
        self.list_element.append(a)
        (self.list_element[-1]).p =process
        (self.list_element[-1]).start=start
        (self.list_element[-1]).end = end
    def end(self,process,start,end,check=0):
        self.put_element(process, start, end)
        process.burst_time=0
        check +=1
        return check
    def calc(self):
        self.begin()
        if self.preemptive==0:
            for i in range(len(self.list_process)):
                a=element()
                self.list_element.append(a)
                (self.list_element[i]).p=self.list_process[i]
        else:
            check=0
            a = 0
            while len(self.list_process)!=check:
                compared=self.according_to_arrival[a]
                for i in self.according_to_arrival[a+1:]:
                    if (i.arrival_time-compared.arrival_time) == compared.burst_time : # b4of eli bkarno (compared) y5ls fel gap eli mbena wla la2
                        check=self.end(compared,compared.arrival_time,i.arrival_time,check)
                        break
                    elif (i.arrival_time-compared.arrival_time) > compared.burst_time: # el gab kpera
                        check = self.end(compared, compared.arrival_time, compared.arrival_time + compared.burst_time, check)
                        if self.according_to_arrival.index(compared)==0:
                            break
                        temp=self.according_to_arrival[:self.according_to_arrival.index(i)-1]
                        gab=i.arrival_time-compared.arrival_time -compared.burst_time
                        if len(temp)!=0:
                            for back in self.according_to_arrival [:self.according_to_arrival.index(i)-1] :
                                new_arrival=compared.arrival_time+compared.burst_time # el gab lazm tt8yar wel arrival lazm yt8yar
                                if back.burst_time ==gab:
                                    check = self.end(back, new_arrival,i.arrival_time ,check)
                                    break
                                elif back.burst_time >gab:
                                    self.put_element(back, new_arrival,i.arrival_time)
                                    back.burst_time -= gab
                                    break
                                else:
                                    check=self.end(back, new_arrival,new_arrival + back.burst_time,check )
                                    new_arrival += back.burst_time
                                    gab -= back.burst_time
                        break
                    else:# kda eli ablya m4 by5ls fel gab
                        if i.burst_time<compared.burst_time:# na el burst bta3y as8r mn el compared fa hw2f el compared
                            self.put_element(compared,compared.arrival_time,i.arrival_time-compared.arrival_time)
                            compared.burst_time -=i.arrival_time-compared.arrival_time
                            compared = i
                            a=self.according_to_arrival.index(i)
                for i in self.according_to_arrival :
                    if i.burst_time==0:
                        del self.according_to_arrival[self.according_to_arrival.index(i)]
                a += 1






