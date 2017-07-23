class Msf(object):

    def __get__(self, obj, typ):
        print "self:{}".format(self)
        print "obj:{}".format(obj)
        print "typ:{}".format(typ)
        return None

    def __set__(self, obj, val):
        print "self:{}".format(self)
        print "obj:{}".format(obj)
        print "val:{}".format(val)
        return None
    

class C1(object):
    def __init__(self):
        self.name = Msf()


if __name__ == "__main__":
    c1 = C1()        
    c1.name = 'wfm'
    print c1.name
    # C1.name = 'wfm'
    # print C1.name


    # c = Msf()
    # c.name = 'wfm'
    # print c.name


