


"""
数组 连续内存空间 线性
insert/pop/find 方法
"""

class Array(object):
    def __init__(self,size):
        self.size = size
        self._data = []
    
    def __setitem__(self,index,value):
        self._data[index] = value
   
    def __getitem__(self,index):
        return self._data[index]
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        for item in self._data:
            yield item
    
    def insert(self,index,value):
        if index == self.size:
                return False
        else:
            self._data.insert(index,value)
   
    def pop(self,index):
        try:
            return self._data.pop(index)
        except IndexError:
            return False

 
    def find(self,index):
        try:
            return self._data[index]
        except IndexError:
            return None





if __name__ == '__main__':
     array = Array(size=32)
     array.insert(0,1)
     assert array[0] == 1
     assert array.pop(1) == False
     assert array.find(1) == False

    
