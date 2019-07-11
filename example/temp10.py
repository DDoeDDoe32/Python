class ParentCls :
    def __init__(self) :
        pass
    def printMethod(self) :
        print('Hello python')

class childClass(ParentCls) :
    def __init__(self) :
        pass

childCls = childClass()
childCls.printMethod()
