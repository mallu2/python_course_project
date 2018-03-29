import numpy as np
class Reflection:
    """
    Class for calculating the reflection of vector a, through the orthogonal matrix of vector v 
    """
    def __init__(self,v): 
        """
        Define the vector v 
        """
        self.v = v
    def __mul__(self, a):
        """
        Calculate the matrix product for the reflection through the plane with matrix H
        """
        gamma = ((np.linalg.norm(self.v))**2)/2
        vvtrans = self.v * np.transpose(self.v)
        H =  np.identity((len(self.v))) - (vvtrans/gamma)
        reflection = np.dot( H, a)
        return(reflection) 
