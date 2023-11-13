<<<<<<< HEAD
from divideAndConquer import MaximumSubarray

if __name__ == '__main__':
  input_str = input("Digite os números do array separados por espaços: ")
  array = [int(x) for x in input_str.split()]
  problem = MaximumSubarray(array)
  max_subarray = problem.find_maximum_subarray()
  max_subarray_sum = sum(max_subarray)
  print("Maior Subarray Contíguo:", max_subarray)
  print("Soma do Maior Subarray Contíguo:", max_subarray_sum)
=======
from divideAndConquer import DivConquer

if __name__ == '__main__':
    array = [-1, 0, 3, 2, -4, 5, -7, 8, -20]
    problem = DivConquer(array)
    print(problem.divide())
>>>>>>> main
