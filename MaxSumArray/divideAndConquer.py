<<<<<<< HEAD
class MaximumSubarray:
    def __init__(self, array):
        self.array = array

    def find_maximum_subarray(self):
        max_value, start, end = self._find_maximum_subarray(0, len(self.array))
        return self.array[start:end]

    def _find_maximum_subarray(self, low, high):
        if low == high - 1:
            return self.array[low], low, low + 1

        middle = (low + high) // 2
        left_max, left_start, left_end = self._find_maximum_subarray(low, middle)
        right_max, right_start, right_end = self._find_maximum_subarray(middle, high)
        crossing_max, crossing_start, crossing_end = self._find_maximum_crossing_subarray(low, middle, high)

        max_value, start, end = max((left_max, left_start, left_end),
                                    (right_max, right_start, right_end),
                                    (crossing_max, crossing_start, crossing_end))

        return max_value, start, end

    def _find_maximum_crossing_subarray(self, low, middle, high):
        left_max_sum = float('-inf')
        left_sum = 0
        left_index = middle

        for i in range(middle - 1, low - 1, -1):
            left_sum += self.array[i]
            if left_sum > left_max_sum:
                left_max_sum = left_sum
                left_index = i

        right_max_sum = float('-inf')
        right_sum = 0
        right_index = middle

        for i in range(middle, high):
            right_sum += self.array[i]
            if right_sum > right_max_sum:
                right_max_sum = right_sum
                right_index = i

        return left_max_sum + right_max_sum, left_index, right_index + 1
=======
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
>>>>>>> main
