class interest:
def __init__(self):
        self.principle=float(raw_input("enter principle"))
        self.rate=float(raw_input("enter ur rate of interest"))
        self.time=int(raw_input("enter time"))
def simple_interest(self):
print "simple interest will be"
print (self.principle*self.rate*self.time)/100;
def compound_interest(self):
print "compound interest is"
print (self.principle*pow((1+(self.rate/100)),self.time)-self.principle)

print "enter 0 to find simple interest and 1 to find compound interest"        
ch=int(raw_input("enter ur choice"))
if(ch==0):
        emp1 = interest()
        emp1.simple_interest()
else:
        emp2=interest()
        emp2.compound_interest()

