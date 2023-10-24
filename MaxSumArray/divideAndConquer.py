class DivConquer:
    def __init__(self, array):
        self.array = array
        self.maxsum = []
        self.soma = int()

    @staticmethod
    def soma(array):
        soma = 0
        for i in array:
            soma += i

    def divide(self, array=None):
        if array is None:
            array = self.array
        if len(array) == 1:
            if array[0] + self.array.soma > self.array.soma:
                self.array.soma = self.array.soma + array[0]
                self.array.maxsum.append(array[0])
                return self.maxsum
            else:
                return self.maxsum
        else:
            print(array)
            self.divide(array[:(len(array) / 2)])
            self.divide(array[(len(array) / 2):])
