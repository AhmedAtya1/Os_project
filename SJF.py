from Scheduler import scheduler


class Sjf(scheduler):

   def p_sort(self):
        k = 0
        time_list=[]
        sorted_list=[]
        for i in self.list_process:
            time_list.append(i.burst_time)
        a=zip(time_list, self.list_process)
        sorted(a)
        for i in a.values:
            self.list_process[k] = i
            k += 1

    def calc(self):
        if self.preemptive==0:
            for i in self.list_process: self.list_element=i
        else :



