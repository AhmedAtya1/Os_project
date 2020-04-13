from Scheduler import scheduler
from Element import element
from copy import deepcopy



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
            Stop = False
            enter=False
            while len(self.list_process)!=check:
                if enter:

                    compared = self.according_to_arrival[a]
                    check = self.end(compared, self.list_element[-1].end,
                                     self.list_element[-1].end + compared.burst_time, check)
                if len(self.according_to_arrival)==1:
                    lis=self.according_to_arrival
                    if len(self.list_element)!=0:
                        start=self.list_element[-1].end
                    else: start=lis[0].arrival_time
                    check=self.end(lis[0], start, start+lis[0].burst_time, check)
                    continue
                compared=self.according_to_arrival[a]
                for i in self.according_to_arrival[a+1:]:
                    Stop = False
                    enter=False
                    if (i.arrival_time-compared.arrival_time) == compared.burst_time : # b4of eli bkarno (compared) y5ls fel gap eli mbena wla la2
                        check=self.end(compared,compared.arrival_time,i.arrival_time,check)
                        break
                    elif (i.arrival_time-compared.arrival_time) > compared.burst_time: # el gab kpera
                        gab = i.arrival_time - compared.arrival_time - compared.burst_time
                        new_arrival = compared.arrival_time + compared.burst_time  # el gab lazm tt8yar wel arrival lazm yt8yar
                        check = self.end(compared, compared.arrival_time, compared.arrival_time + compared.burst_time, check) #end lel compared
                        if (self.according_to_arrival.index(compared)==0)and(self.according_to_arrival.index(i)==1):
                            break
                        temp=self.according_to_arrival[:self.according_to_arrival.index(i)]
                        if len(temp)!=0:
                            for back in self.according_to_arrival [:self.according_to_arrival.index(i)] :
                                if back.burst_time == 0: continue
                                if back.burst_time ==gab:
                                    check = self.end(back, new_arrival,i.arrival_time ,check)
                                    break
                                elif back.burst_time >gab:
                                    self.put_element(back, new_arrival,i.arrival_time)
                                    back.burst_time -= gab
                                    break
                                else:
                                    temp_time=new_arrival+back.burst_time
                                    check=self.end(back, new_arrival,new_arrival + back.burst_time,check )
                                    new_arrival = temp_time
                                    gab -= back.burst_time
                        a = self.according_to_arrival.index(i)
                        break
                    else:# kda eli ablya m4 by5ls fel gab
                        if i.burst_time<compared.burst_time:# na el burst bta3y as8r mn el compared fa hw2f el compared
                            self.put_element(compared,compared.arrival_time,i.arrival_time-compared.arrival_time)
                            compared.burst_time -=i.arrival_time-compared.arrival_time
                            compared = i
                            a=self.according_to_arrival.index(i)
                        else:# kda el compared wa2to as8r mny bs el gab eli mbena m4 m2dyah
                            Stop = True
                    #enter = True
                if Stop :# lo d5lt hna yb2a el process w2ta so8yar bs akpr mn kol el gaps eli mben el arrival times
                    check=self.end(compared,compared.arrival_time,compared.arrival_time+compared.burst_time,check)
                compared=self.according_to_arrival[a]
                delete=[]
                for i in self.according_to_arrival :
                    if i.burst_time==0:
                        delete.append(i)
                for f in delete:
                     self.according_to_arrival.remove(f)
                if Stop:
                    Stop=False
                    n=self.according_to_arrival[0]
                    for o in self.according_to_arrival:
                        if n.burst_time > o.burst_time:
                            n=o
                    a = self.according_to_arrival.index(n)



                #if compared in self.according_to_arrival:
                    #a =self.according_to_arrival.index(compared)
