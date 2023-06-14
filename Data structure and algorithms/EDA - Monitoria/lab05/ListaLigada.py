from No import No

class ListaLigada:
    def __init__(self, type):
        self.head = None
        self.tail = None
        self.type = type # 1 = inserção inicio, 2 = inserção final, 3 = ordenada
        self.occur = 0

    def insert(self, value):
        self.occur +=1
        new_node = No(value)
        
        if(self.type == 1):
            if(not self.head):
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        elif(self.type == 2):
            if(not self.head):
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
        elif(self.type == 3):
            if(not self.head):
                self.head = new_node
                self.tail = new_node
            else:
                if(self.head.value > new_node.value):
                    new_node.next = self.head
                    self.head = new_node
                else:
                    current = self.head
                    while(current.next != None and current.next.value < new_node.value):
                        current = current.next
                    aux = current.next
                    current.next = new_node
                    current.next.next = aux
    
    def remove(self, value):
        if(self.head.value == value):
            aux = self.head.next
            del self.head
            self.head = aux
        else:
            parent = self.head
            current = self.head.next
            while(current != None and current.value != value):
                parent = parent.next
                current = current.next
            if(not current):
                print("objeto nao encontrado")
            else:
                aux = current.next
                del current
                parent.next = aux

    def search(self, value):
        current = self.head
        while (current):
            if (current.value == value):
                return True
            current = current.next
        return False







        
    def print(self):
        current = self.head
        while(current):
            print(current.value, " ", sep="", end="")
            current = current.next
        print(" ")

           