class Matrix_operations:
    """
    Class for matrix operarations
    """
    def arrayn(mn):
        """
        Return number of rows
        """
        return(np.shape(mn)[0])
    def arraym(mn):
        """
        Return number of columns
        """
        return(np.shape(mn)[1])
    def array_of_columns(mn):
        """
        Return columns
        """
        arrayn = np.shape(mn)[0]
        arraym = np.shape(mn)[1]
        for b in range(arraym):
            columns =(np.hsplit(mn, mn.shape[1]))
            return(columns)
