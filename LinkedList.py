from Node import Node

class LinkedStack :
    def __init__(self):self.head = None                          #데이터 멤버로는 시작 노드를 가리키는 head만!
    def isEmpty(self) : return self.head == None                # head가 None이면 공백!(연결된 스택과 같다)
    def isFull(self) : return False                             #연결된 스택과 같다
    
    def clear(self): self.head =None                             #리스트 초기화

    def getNode(self,pos) :                                     #시작 노드에서부터 pos번 링크를 따라 움직이면  pos위치에 도착!
        if pos<0 : return None
        node = self.head
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self,pos) :                                     #getNode(pos)먼저 호출해야 함!
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data


    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :                         #공백이면 시작 위치에 삽입
            self.head = Node(elem, self.head)
        else :                                      #공백이 아니면 
            node = Node(elem,before.link)           #node를 만들고 link는 before다음 링크를 가리키도록
            before.link = node                      #이전 노드 before가 새로운 node를 가리킨다

    def delete(self,pos) :
        before = self.getNode(pos-1)
        if before == None :                         #before가 None이라는 것은 시작노드를 삭제하는 상황인 것
            if self.head is not None :              #head는 None이 아니고 pos-1이 가리키는 값이 None이라는 것은 pos가 시작값(머리노드)이라고 생각함
                self.head = self.head.link
        elif before.link != None :                  #before의 link가 삭제할 노드의 다음 노드를 가리키도록 함
            before.link = before.link.link
        
    def size(self) :
        node = self.head      #연결된 스택과 같다
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count