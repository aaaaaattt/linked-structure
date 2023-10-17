class Node:
    def __init__(self,elem,link=None): #링크는 default값으로 None사용
        self.data = elem #노드 데이터 필드
        self.link - link #노드 링크 필드

class LinkedStack :
    def __init__(self):
        self.top = None #연결된 스택의 생성자의 데이터 멤버에는 시작 노드를 가리키는 top뿐!
        
    def isEmpty(self):
        return self.top == None #공백상태는 top이 None인 경우
    
    def isFull(self):
        return False #포화상태는 항상 False 반환, 왜냐하면 용량이 없으므로!
    
    def push(self, e):              #삽입 연산
        self.top = Node(e,self.top) # 새로운 노드 생성
                                    # 기존 top이 가리키는 것은 새로 생긴 link가 받고
                                    # top은 새로 생성된 노드를 가리키도록 함

    def pop(self) :                 #삭제 연산                                    #
        if not self.isEmpty():      #공백 검사
            n = self.top            # n이 현재 상단을 가리키게 하고
            self.top = n.link            # 다시 top은 n을 가리키고
            return n.data           # n의 데이터 반환
        
    def peek(self):
        if not self.isEmpty():
            return self.top.data #공백이 아니면 머리노드의 데이터 반환
        
    def size(self) :
        node = self.top
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count