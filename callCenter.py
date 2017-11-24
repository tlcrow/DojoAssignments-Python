class Call(object):
    def __init__ (self, unique_id, name, phone_number, time_call, reason_call):
        self.call = [unique_id, name, phone_number, time_call, reason_call]

    def display(self):
        print self.call

class CallCenter(Call):
    def __init__(self):
        self.calls = []
        self.queue = 0
    
    def add(self, unique_id, name, phone_number, time_call, reason_call):
        super(CallCenter, self).__init__(unique_id, name, phone_number, time_call, reason_call)
        self.calls.append(self.call)
        self.queue += 1
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue -= 1
        return self

    def info(self):
        for i in self.calls:
            print i[1], i[2]
        print "Queue: ", self.queue

    def removePhone(self, phone_number):
            for i in range(self.queue-1):
                if self.calls[i][2] == phone_number:
                    self.calls.pop(i)
                    self.queue -= 1
                    i -= 1
            return self
    
    def sortQueue(self):
        self.calls = sorted(self.calls, key=lambda x:x[3])
        return self


callcenter = CallCenter()
callcenter.add(1,"Isaac","802-380-3564","05:56","blah blah")
callcenter.add(2,"Helen","Helen's Number","02:57","IT struggles")
callcenter.add(3,"Amanda","Amanda's Number","12:57","Python not working")
callcenter.add(4,"Rob","Rob's Number","01:57","just sad")
callcenter.add(5,"Isadsafac","089-asdf-3564","10:57","who knows")
callcenter.remove().removePhone("Rob's Number").sortQueue().info()
