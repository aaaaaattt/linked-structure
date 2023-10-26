class Node: #Node 모듈
    def __init__(self,elem,link=None):  #링크는 default값으로 None사용
        self.data = elem                #노드 데이터 필드
        self.link = link                #노드 링크 필드