from Process import process
class element :
    p=process()
    start=0.0
    end=0.0
    duration=0.0

    def __repr__(self):
        return 'process name: %s start: %s end: %s'%(self.p.name,str(self.start),str(self.end))



