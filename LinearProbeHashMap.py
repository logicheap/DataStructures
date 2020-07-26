class Item:
    def __init__(self, k, v):
        self._key = k
        self._value = v

class LinearProbeHashMap:
    def __init__(self, capacity=11):

        #Creates a list of size CAPACITY and initialize it with None
        self._table = [None]*capacity

        #Keeping the count of total entries in table
        self._n = 0

    def _hash_function(self, key):
        return key%len(self._table)

    def __len__(self):
        return self._n

    def _find_bucket(self, key, hashed_key):
        while True:
            if self._table[hashed_key] is not None:
                if self._table[hashed_key]._key == key:
                    return hashed_key, True
                hashed_key = (hashed_key + 1)%len(self._table)
            else:
                return hashed_key, False

    def __getitem__(self, key):
        hashed_key = self._hash_function(key)
        hashed_key, found = self._find_bucket(key, hashed_key)
        if found is False:
            raise KeyError("key error")
        return self._table[hashed_key]._value

    def __setitem__(self, key, value):
        hashed_key = self._hash_function(key)
        hashed_key, found = self._find_bucket(key, hashed_key)
        self._table[hashed_key] = Item(key, value)
        if found is False:
            self._n += 1

        if self._n > len(self._table)//2:
            self._resize(2*len(self._table)-1)

    def _resize(self, capacity):
        old = []
        for bucket in self._table:
            if bucket is not None:
                old.append(bucket)
        self._table = capacity*[None]
        self._n = 0
        for items in old:
            self[items._key] = items._value

    def print(self):
        for i in range(len(self._table)):
            if self._table[i] is not None:
                print("..............................")
                print("At " + str(i))
                print(str(self._table[i]._key) + " " +  str(self._table[i]._value))

testHashMap = LinearProbeHashMap()

print("size of table is "+ str(len(testHashMap._table)))
#Testing set function
testHashMap[10] = "John"
testHashMap[21] = "Ram"
testHashMap[24] = "Aman"




#Testing resize function
testHashMap[22] = "Jyoti"
testHashMap[23] = "Kate"
testHashMap[3] = "Phoebe"
testHashMap[4] = "Jyotishi"
#testHashMap[56] = "Kate"
#testHashMap[34] = "Phoebe"
#testHashMap[18] = "Jyoti"
#testHashMap[23] = "Kate"
#testHashMap[39] = "Phoebe"
#testHashMap[13] = "Jyoti"
#testHashMap[29] = "Kate"
#testHashMap[37] = "Phoebe"

#Testing get function
print("value for key 21 is: " + testHashMap[21])
#print("value for key 25 is: " + testHashMap[25])

testHashMap.print()
#Check size of table
print("size of table is "+ str(len(testHashMap._table)))
