class DivConquer:
    def __init__(self, array):
        self.array = array
        self.maxsum = []
        self.sum = int(0)

    def soma(self, subarray):
        soma = 0
        for i in subarray:
            soma += i
        if soma > self.sum:
            self.sum = soma
            self.maxsum = subarray
            return True
        else:
            return False

    def divide(self, array=None):
        if array is None:
            array = self.array
        meio = int(len(array)/2)

        if len(array) == 1:
            print("\t",array)
            if self.soma(array):
                return self.maxsum
        else:
            print(array)
            self.divide(array[:meio])
            self.divide(array[meio:])
