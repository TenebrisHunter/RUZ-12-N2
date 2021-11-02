# Как определять классы Python
# Пример файла для работы с классами
class myClass():
  def method1(self):
      print ("Guru99")
        
  def method2(self,someString):    
      print ("Software Testing:" + someString)
      
   
      
def main():           
  # методы класса
  c = myClass ()
  c.method1()
  c.method2(" Testing is fun")
  
if __name__== "__main__":
  main()
 
 
#Как работает наследование
# Пример файла для работы с классами
class myClass():
  def method1(self):
      print "Guru99"
        
      
class childClass(myClass):
  #def method1(self):
        #myClass.method1(self);
        #print "childClass Method1" 
        
  def method2(self):
        print "childClass method2"     
         
def main():           
  # методы класса
  c2 = childClass()
  c2.method1()
  #c2.method2()
 
if __name__== "__main__":
  main()