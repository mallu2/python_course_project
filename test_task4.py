#import modules
import numpy as np
from Task4 import Reflection
from Task4 import Matrix_operators

b = np.array([1,2,3])
b = b.reshape(3,1)
print(b)
c = np.matrix([2,3,4,(-2),4,7,5,9,1,6,-3,-1])
c = c.reshape(4,3)
print(c)

#test_Matrix=Matrix_operations.array_of_columns(c)[1]
#print(test_Matrix)

r = Reflection(b)
result = r * c
print(result)
