import numpy as np


#define the function
def calculate(list):
  #check if the lenght of the input is 9
  if len(list) != 9:
    #raising error message if the condition is not met
    raise ValueError('List must contain nine numbers.')
  #if the conditional is met we create and array witht he list
  arr = np.array(list).reshape(3, 3)
  #calculate the numbers we need using numpy
  calculations = {
    'mean': [
      np.mean(arr, axis=0).tolist(),
      np.mean(arr, axis=1).tolist(),
      np.mean(arr).tolist()
    ],
    'variance': [
      np.var(arr, axis=0).tolist(),
      np.var(arr, axis=1).tolist(),
      np.var(arr).tolist()
    ],
    'standard deviation': [
      np.std(arr, axis=0).tolist(),
      np.std(arr, axis=1).tolist(),
      np.std(arr).tolist()
    ],
    'max': [
      np.max(arr, axis=0).tolist(),
      np.max(arr, axis=1).tolist(),
      np.max(arr).tolist()
    ],
    'min': [
      np.min(arr, axis=0).tolist(),
      np.min(arr, axis=1).tolist(),
      np.min(arr).tolist()
    ],
    'sum': [
      np.sum(arr, axis=0).tolist(),
      np.sum(arr, axis=1).tolist(),
      np.sum(arr).tolist()
    ]
  }
  return calculations
