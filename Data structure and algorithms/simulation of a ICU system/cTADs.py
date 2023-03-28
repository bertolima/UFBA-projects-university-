class Elemento:

  def __init__(self, elem, prox=None):

    self.elem = elem
    self.prox = prox
    
  def __str__(self):
    return f'{self.elem}' 
    
  def getElem(self):
    return self.elem

class Elemento2:
  
  def __init__(self, elem, antElem=None):

    self.elem = elem
    self.antElem = antElem
    
  def __str__(self):
    return f'{self.elem}' 
    
  def getElem(self):
    return self.elem

class queue:

    def __init__(self):
      self.queue = []

    def isEmpty(self):
      return len(self.queue) == 0

    def insert(self, item):
      self.queue.append(item)
    
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i].getStage() > self.queue[max_val].getStage():
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()

    def remove(self):
      return self.queue.pop()
      
    def getLen(self):
      return len(self.queue)


class stack:
  
    def __init__(self):
        
      self.top = None
      self.nElement = 0  
      self.verificarPilha = False
      

    def pull(self, elemento):
      self.verificarPilha = True
      novoElem = Elemento2(elemento)

      novoElem.antElem = self.top
      
      self.top = novoElem
      self.nElement +=1
      
    def pop(self):
      if self.top is None:
        return False
      else:
        self.top = self.top.antElem
        self.nElement -=1
        if self.top is None:
          self.verificarPilha = False

    def isEmpty(self):
      if self.nElement == 0:
        return True
      return False
    
    def getTop(self):
      if self.top is not None:
        return self.top.getElem()
        
    def __str__(self):
      return f'{self.top}'
    def getLen(self):
      return self.nElement

class normalQueue:

    def __init__(self):
        self.first = None
        self.last = None
        self.nElement = 0

    def __str__(self):
        return f'{self.first}' 

    def set(self, elem):
        novo_elem = Elemento(elem)
        self.nElement += 1
        if self.first == None:
            self.first = novo_elem
            self.last = novo_elem
        else:
            self.last.prox = novo_elem
            self.last = novo_elem
    def isEmpty(self):
      if self.nElement == 0:
        return True
      return False
            
    def get(self):
        return self.first.getElem()

    def remove(self):
        self.nElement -= 1
        if self.first == None:
            self.last = None
            return
        self.first = self.first.prox
    def getLen(self):
        return self.nElement

