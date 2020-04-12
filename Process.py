class process :
    pr=0
    arrival_time=0
    burst_time=0
    name=''
    def __repr__(self):
        return self.name +' burst time = '+str(self.burst_time)+' arrival time = '+str(self.arrival_time)+' priority = '+str(self.priority)