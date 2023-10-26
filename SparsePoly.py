from LinkedList import LinkedList

class Term :
    def __init__(self,coef,expo):
        self.coef = coef
        self.expo = expo
    
class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__
        self.coef = []  #계수
        self.expo = []  #지수


    def read(self): #입력
        inp1,inp2 = input("계수 차수 입력(종료:-1)").split()
        inp1 = int(inp1)
        inp2 = int(inp2)
        a = Term(inp1,inp2)
        self.expo.append(a.expo)
        self.coef.append(a.coef)
        
        while(inp1 != -1 and inp2 != -1):
            inp1,inp2 = input("계수 차수 입력(종료:-1)").split()
            inp1 = int(inp1)
            inp2 = int(inp2)
            a = Term(inp1,inp2)
            if(inp1 == -1):
                break;
            self.expo.append(a.expo)
            self.coef.append(a.coef)
            
    
    def display(self):#출력
        num = len(self.coef)
        print("입력 다항식 :",end='')
        for i in range (0,num):
            print(f"{self.coef[i]}x^{self.expo[i]} +",end=' ')
    
    def add(self,polyB):#다항식 덧셈 함수
        num1 = len(self.coef)
        print("A = ",end='')
        for i in range (0,num1):
            print(f" {self.coef[i]}x^{self.expo[i]} +",end=' ')
        print()
        num2 = len(polyB.coef)
        print("B = ",end='')
        for i in range (0,num2):
            print(f"{polyB.coef[i]}x^{polyB.expo[i]} +",end=' ')
        print()

        c = SparsePoly()
        Self_lastIndex = len(self.expo)-1
        polyB_lastIndex = len(polyB.expo)-1
        self_innerIndex = 0
        polyB_innerIndex = 0
        count = 0
        try: #예외 처리문
            while(self_innerIndex <= Self_lastIndex or polyB_innerIndex<=polyB_lastIndex):        
                if(self.expo[self_innerIndex]>polyB.expo[polyB_innerIndex]):
                    c.coef.append(self.coef[self_innerIndex])
                    c.expo.append(self.expo[self_innerIndex])
                    self_innerIndex += 1
                    
                
                elif(self.expo[self_innerIndex]==polyB.expo[polyB_innerIndex]):
                    c.coef.append(self.coef[self_innerIndex]+polyB.coef[polyB_innerIndex])
                    c.expo.append(self.expo[self_innerIndex])
                    polyB_innerIndex += 1
                    self_innerIndex +=1
                    
                
                elif(self.expo[self_innerIndex]<polyB.expo[polyB_innerIndex]):
                    c.coef.append(polyB.coef[polyB_innerIndex])
                    c.expo.append(polyB.expo[polyB_innerIndex])
                    polyB_innerIndex += 1
                    

        except:
            if(self_innerIndex > Self_lastIndex):  
                while(polyB_innerIndex<=polyB_lastIndex):
                    c.coef.append(polyB.coef[polyB_innerIndex])
                    c.expo.append(polyB.expo[polyB_innerIndex])
                    polyB_innerIndex += 1
                    

            elif(polyB_innerIndex > polyB_lastIndex):
                while(self_innerIndex<=Self_lastIndex):
                    c.coef.append(self.coef[self_innerIndex])
                    c.expo.append(self.expo[self_innerIndex])
                    self_innerIndex += 1
                    
                
        print("A+B =",end=' ')
        
        for i in range (0,len(c.coef)):
            print(f"{c.coef[i]}x^{c.expo[i]} +",end=' ')
        print()


    
        

a = SparsePoly()
a.read()
a.display()
print()
b = SparsePoly()
b.read()
b.display()
print()
a.add(b)



        
            


    # def add(self,polyB): #다항식 덧셈



