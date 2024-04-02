import numpy as np

#filter array
arr1=np.array([1,22,55,56])
listFilter= arr1 %2==0
arr2=arr1[listFilter]
print(arr2)