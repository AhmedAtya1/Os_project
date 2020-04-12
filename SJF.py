from Scheduler import scheduler
class sjf(scheduler):
    def p_sort(self):
        time_list=[]
        sorted_list=[]
        for i in self.list_process:
            time_list.append(i.burst_time)
        a=zip(time_list, self.list_process)
        sorted(a)








