class DNode:
    def __init__ (self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self) :
        self.front = None
        self.rear = None

    def addFront(self, item):   #전단 삽입 연산
        node = DNode(item, None, self.front)    #새로운 노드 생성 시 next에는 front가 가리키는 값을 가리키도록!
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node  #기존의 노드가 가리키는 prev값은 새로운 node를 가리키도록
            self.front = node       #front도 새로 생긴 node를 가리키도록
    
    def addRear(self, item):    #후단 삽입 연산
        node = DNode(item, self.rear, None) #전단 삽입연산과 반대과정!
        if(self.isEmpty()):
            self.front = self.rear = node
        else : 
            self.rear.next = node
            self.rear = node
    
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data          #삭제할 노드(front)의 데이터 복사 
            self.front = self.front.next    #front를 다음으로 옮김
            if self.front == None :         #front가 공백이면 rear도 공백    
                self.rear = None
            else :
                self.front.prev = None      #front의 이전 노드는 None
            return data                     #데이터 반환
    
    def deleteRear(self) :
        if not self.isEmpty():
            data = self.rear.data           #삭제할 노드(front)의 데이터 복사
            self.rear = self.rear.prev      #rear를 이전으로 옮김
            if self.rear == None:           #front가 공백이면 rear도 공백    
                self.front = None           
            else:                           
                self.rear.next = None       #rear의 다음 노드는 None
            return data                     #데이터 반환 
