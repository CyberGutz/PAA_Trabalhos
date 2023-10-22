class divConq:
    def __init__(self, array):
        self.array = list(int(array))
        self.maxsum = []
    
    def divide(self, array = None):
        if array == None:
            array = self.array
            if len(array) == 1:
                return
            else:
                self.divide(array[:len(array)/2])
                self.divide(array[len(array)/2:])
                