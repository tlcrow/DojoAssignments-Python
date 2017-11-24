# Part I
class Mathdojo(object):
    def __init__(self):
        self.num = 0
    
    def mathadd(self, *addnum):
        for i in addnum:
            self.num += i
        return self
   
    def mathsub(self, *subnum):
        for i in subnum:
            self.num -= i
        return self

    def result(self):
        print self.num
        return self.num

# md = Mathdojo()
# md.mathadd(2).mathadd(2, 5).mathsub(3, 2).result()

# Part II and III
class Mathdojo(object):
    def __init__(self):
        self.num = 0
    
    def mathadd(self, *addnum):
        for i in addnum:
            if type(i) == list or type(i) == tuple:
                self.num += sum(i)
            else:
                self.num += i
        return self
   
    def mathsub(self, *subnum):
        for i in subnum:
            if type(i) == list or type(i) == tuple:
                self.num -= sum(i)
            else:
                self.num -= i
        return self

# md2 = Mathdojo()
# print md2.mathadd([1],3,4).mathadd([3, 5, 7, 8], [2, 4.3, 1.25]).mathsub(2, [2,3], [1.1, 2.3]).num