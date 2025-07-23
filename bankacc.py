class Bank_Acc:
    def __init__(self):
        pass
    def add_data(self):
        print("Enter your acc no")
        self.accno  = input()
        print("Enter your pin number")
        self.pin = input()

acc1 = Bank_Acc()
acc1.add_data()
print("your pin is ", acc1.pin)
    
