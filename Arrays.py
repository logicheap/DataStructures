import ctypes

class Arrays:
    def __init__(self):
        self._n = 0  #counts current number of elements
        self._capacity = 1   #Capacity = total number of blocks reserved for elements
        self._A = _create_array(self._capacity)

    def insert(self, obj, index):
        """Add object to the specified index of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        if index >= self._n:
            raise IndexError('invalid index')
        for i in range(self._n, index, -1):
            self._A[i] = self._A[i - 1]
        self._A[index] = obj
        self._n += 1

    def delete(self, index):
        """Delete object from the specified index of the array."""
        if (index >= self._n) or (index < 0):
            raise IndexError('invalid index')
        for i in range(index, self._n - 1):
            self._A[i] = self._A[i + 1]
        self._n -= 1

    def print_array_details(self):
        "Prints array, capacity and length"
        print("------------------------------------------")
        print("Length of array is " + str(self._n))
        print("Capacity of array is " + str(self._capacity))
        print("Array is ")
        for i in range(self._n):
            print(str(self._A[i]) + " ")
            
    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c
        
    def _create_array(self,c):
        return (ctypes.py_object * c)()

A = Arrays()
A.print_array_details()
A.insert(2,0)
A.print_array_details()
A.delete(0)
A.print_array_details()
A.append(5)
A.append(15)
A.print_array_details()
