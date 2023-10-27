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

    def degree(self):
        return self.expo[0] #최고차항의 차수는 리스트의 첫번째에!


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
            
    def evaluate(self,n): #수식연산 (Ex. f(x) = x^2 + x --> f(2) = 2^2 + 2 = 10)
        Rsum = 0
        for i in range(len(self.coef)):
            Tsum = self.coef[i]
            for count in range(0,self.expo[i]):
                Tsum *= self.expo[i]
            Rsum += Tsum
            print("Rsum=",Rsum)
        
        
        return Rsum

    
    def display(self):#출력
        num = len(self.coef)
        print("입력 다항식 :",end='')
        for i in range (0,num):
            print(f"{self.coef[i]}x^{self.expo[i]} +",end=' ')
    
    def __add__(self, polyB):
        Self_lastIndex = len(self.expo)-1
        polyB_lastIndex = len(polyB.expo)-1
        self_innerIndex = 0
        polyB_innerIndex = 0
        count = 0
        try: 
            while(self_innerIndex <= Self_lastIndex or polyB_innerIndex<=polyB_lastIndex):        
                if(self.expo[self_innerIndex]>polyB.expo[polyB_innerIndex]):
                    c.coef.append(self.coef[self_innerIndex])
                    self_innerIndex += 1
                    
                
                elif(self.expo[self_innerIndex]==polyB.expo[polyB_innerIndex]):
                    self.coef[self_innerIndex]=self.coef[self_innerIndex]+=polyB.coef[polyB_innerIndex]
                    polyB_innerIndex += 1
                    self_innerIndex +=1
                    
                
                elif(self.expo[self_innerIndex]<polyB.expo[polyB_innerIndex]):
                    c.coef.append(polyB.coef[polyB_innerIndex])
                    polyB_innerIndex += 1
                    

        except:#예외 처리문
            if(self_innerIndex > Self_lastIndex):  
                while(polyB_innerIndex<=polyB_lastIndex):
                    c.coef.append(polyB.coef[polyB_innerIndex])
                    polyB_innerIndex += 1
                    

            elif(polyB_innerIndex > polyB_lastIndex):
                while(self_innerIndex<=Self_lastIndex):
                    c.coef.append(self.coef[self_innerIndex])
                    self_innerIndex += 1
    
    def add(self,polyB):            #다항식 덧셈 함수 , 시간복잡도는 O(n^2)
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
        try: 
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
                    

        except:#예외 처리문
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

print(a.evaluate(3))

#print("차수 : "a.degree())
# a.display()
# print()
# b = SparsePoly()
# b.read()
# b.display()
# print()
# a.add(b)



        
            