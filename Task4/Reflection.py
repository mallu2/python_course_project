import numpy as np
class Reflection:
    """
    Class for calculating the reflection of a, through the orthogonal matrix of v 
    """
    def __init__(self, v): 
        """
        Define the vector v
        """
        self.v = v  
    
    def __mul__(self, a):
        """
        Calculate the matrix product for the 
        reflection of vector a or the vectors 
        resulting from the columns in matrix a through 
        the plane of the orthogonal matrix H
        """
        if len(a) < len(self.v):
            raise Exception('Length of a is smaller than length of v!')
        elif len(a) > len(self.v):
            differenceav = (len(a) - len(self.v))
            add = np.zeros(differenceav)
            vresh = self.v.reshape(1,len(self.v))
            velong = np.insert(self.v,0,add).reshape(len(a),1)
            self.v = velong
        else:
            self.v = v
        gamma = ((np.linalg.norm(self.v))**2)/2
        vvtrans = self.v * np.transpose(self.v)
        H =  np.identity((len(a))) - (vvtrans/gamma)
        reflection = np.dot(H,a)
        return(reflection) 
