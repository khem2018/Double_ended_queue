class Deque(_DoublyLinkedListBase):
    def firstElement(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._frontEnd._next._data
    
    def lastElement(self):
        if self.is_empty():
            raise Excpetion('deque is empty')
        return self._rareEnd._previous._data
    
    def addFirst(self,data):
        ''' add element at the front end of the deque'''
        self._insertBetween(data,self._frontEnd,self._frontEnd._next)
        
    def addLast(self,data):
        '''add element at the read end of the deque'''
        self._insertBetween(data,self._rareEnd._previous,self._rareEnd)
    
    def deleteFirst(self):
        ''' delete a node from the deque and return node data'''
        if self.is_empty():
            raise Exception('deque is empty')
        return self._deleteNode(self._frontEnd._next)
    
    def deleteLast(self):
        if self.is_empty():
            raise Exception('deque is empty')
        return self._deleteNode(self._rareEnd._previous)
    
    def get_size(self):
        return self.__len__()
    
    def print_dqueue(self):
        curr = self._frontEnd._next
        counter = self.get_size()
        while counter>0:
            print(curr._data)
            curr= curr._next
            counter-=1
