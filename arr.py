import numpy as np
marks=[5,7,9,32,21]
print("list:",marks)
array=np.array(marks)
print("array:",array)
print("size:",array.size)
print("datatype:",array.dtype)
print("dimension:",array.ndim)
print("shape:",array.shape)
print("highest marks:",np.max(array))
print("lowest marks:",np.min(array))
average=np.mean(array)
print("class average is:",average)
print(np.where(array>4,"pass","fail"))
print("class performance:",np.where(average<5,"below average","above average"))



