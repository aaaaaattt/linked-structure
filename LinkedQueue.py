from Node import Node

class LinkedQueue:
    def __init__(self) :
        self.tail = None
        def isEmpty(self) : return self.tail == None #tail이 None이면 공백
        def isFull(self) : return False             #역시나 포화상태는 의미없다
        
    def enqueue(self, item) :
        node = Node(item, None)     #삽입할 노드
        if self.isEmpty() :         #case1.공백 상태에서 삽입
            self.tail = node        #tail은 새로운 노드를 가리키고 
            node.link = node        #node.link는 자기 자신을 가리키도록
        else :
            node.link = self.tail.link #case2. 공백이 아닌 상태에서 삽입
            self.tail.link = node      #tail의 링크가 n을 가리킨다 -> tail이 가리키고 있는 후단의 링크가 n을 가리키도록 한 것
            self.tail = node

    def dequeue(self) :
        if not self.isEmpty():
            data = self.tail.link.data #반환할 데이터 저장
            if self.tail.link == self.tail :       #case1) 큐의 요소가 하나인 경우의 삭제
                self.tail = None
            else:
                self.tail.link = self.tail.link.link #case2) 요소가 여러개인 경우 삭제
            return data 