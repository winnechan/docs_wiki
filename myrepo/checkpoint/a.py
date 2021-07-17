class A:
   empCount = 0
 
   def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        A.empCount += 1
   
   def displayCount(self):
        '''
        help docs 
        '''
        print("Total Employee %d" % A.empCount)
 
   def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)