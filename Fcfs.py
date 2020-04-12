from Scheduler import scheduler
from Element import element
import operator
class fcfs (scheduler):
    def calc(self):
        self.list_process.sort(key=operator.attrgetter('arrival_time'))
        for i in range(len(self.list_process)):
            a = element()
            self.list_element.append(a)
            (self.list_element[i]).p = self.list_process[i]