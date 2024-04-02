import numpy as np

list1=[1,2,3,4,5,6,7,8]
arr1=np.array(list1)

print(arr1.dtype)
print(arr1.astype('U5'))

arr3=np.array([334,5,56,768,5])
arr2=arr1.copy()
arr2=np.append(arr3,arr1)
print(arr2)

arr4=arr1.view()
print(arr4)
arr4=np.append(arr3,arr1)
print(arr4)

list5=[[1,2,3],[4,5,6],[7,8,9]]
arr5=np.array(list5)
print(list5)
print(arr5)
print(arr5.ndim)
print(arr5.shape)

list6=[[8,9,1],[14,51,63],[37,86,69]]
arr6=np.array(list6)
arr7=np.concatenate((arr6,arr5),axis=1)
print(arr7)
arr7=np.concatenate((arr6,arr5))
print(arr7)

arr8=np.stack((arr5,arr6))
print(arr8)
print(np.array_split(arr6,3))

print(np.where(arr1 %2==0))

print('in array',np.searchsorted(arr1,3,side='right'))
