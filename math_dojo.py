class Mathdojo(object):
    def __init__(self):
        self.value = 0
    def add(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for numeral in arg:
                    self.value += numeral
            else:
                self.value += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for numeral in arg:
                    self.value -= numeral
            else:
                self.value -= arg
        return self
    def result(self):
        print 'Number: ' + str(self.value)
        return self

md = Mathdojo()

# md.add(2).add(2,5).subtract(3,2).result()
md.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], [1.1,2.3]).result()