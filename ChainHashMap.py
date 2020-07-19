class Item:
    def __init__(self, k, v):
        self._key = k
        self._value = v

class ChainHashMap:
    def __init__(self, capacity=7):

        #Creates a list of size CAPACITY and initialize it with None
        self._table = [None]*capacity

        #Keeping the count of total entries in table
        self._n = 0

    def _hash_function(self, key):
        return key%len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        hashed_key = self._hash_function(key)
        if self._table[hashed_key] is None:
            raise KeyError("key error")
        else:
            for item in self._table[hashed_key]:
                if item._key == key:
                    return item._value
            raise KeyError("key error")

    def __setitem__(self, key, value):
        hashed_key = self._hash_function(key)
        if self._table[hashed_key] is None:
            self._table[hashed_key] = []
        for item in self._table[hashed_key]:
            if item._key == key:
                item._value = value
                return

        self._table[hashed_key].append(Item(key,value))
        self._n += 1

        if self._n > len(self._table)//2:
            self._resize(2*len(self._table)-1)

    def _resize(self, capacity):
        old = []
        for bucket in self._table:
            if bucket is not None:
                for items in bucket:
                    old.append(items)
        self._table = capacity*[None]
        self._n = 0
        for items in old:
            self[items._key] = items._value

    def print(self):
        for i in range(len(self._table)):
            if self._table[i] is not None:
                print("..............................")
                print("At " + str(i))
                for item in self._table[i]:
                    print(str(item._key) + " " +  str(item._value))






testHashMap = ChainHashMap()

print("size of table is "+ str(len(testHashMap._table)))
#Testing set function
testHashMap[10] = "John"
testHashMap[21] = "Ram"
testHashMap[24] = "Aman"

#Testing get function
print("value for key 24 is: " + testHashMap[24])
#print("value for key 25 is: " + testHashMap[25])


#Testing resize function
testHashMap[1] = "Jyoti"
#testHashMap[2] = "Kate"
#testHashMap[3] = "Phoebe"
#testHashMap[8] = "Jyoti"
#testHashMap[56] = "Kate"
#testHashMap[34] = "Phoebe"
#testHashMap[18] = "Jyoti"
#testHashMap[23] = "Kate"
#testHashMap[39] = "Phoebe"
#testHashMap[13] = "Jyoti"
#testHashMap[29] = "Kate"
#testHashMap[37] = "Phoebe"

testHashMap.print()
#Check size of table
print("size of table is "+ str(len(testHashMap._table)))
