class sortedArrayList :
    def __init__(self,capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def __str__(self):
        return str(self.array[:self.size])
    
    def contains(self,e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False
    
    def insert(self,e):
        if self.contains(e) or self.isFull():
            return 
        self.array[self.size] = e
        for i in range(self.size-1 , 0, -1):
            if self.array[i-1] < self.array[i]:
                break
            self.array[i-1],self.array[i] = self.array[i], self.array[i-1]

    def delete(self,e):
        if not self.contains(e) or self.isEmpty():
            return 
        i = 0
        while self.array[i] < e :
            i += 1
        self.size -= 1
        while i < self.size :
            self.array[i] = self.array[i+1]
            i += 1
        self.array[self.size] = None
    
    