class Bank_Acc:
    def __init__(self):
        pass
    def add_data(self):
        print("Enter your acc no")
        self.accno  = input()
        print("Enter your pin number")
        self.pin = input()
    def show_pin(self):
        print("Enter the OTP to see the pin")
        otp = int(input())
        if otp == 7878:
            print("Your pin is ", slef.__pin)
        else:
            print("Invalid OTP")

acc1 = Bank_Acc()
acc1.add_data()
acc1.show_pin()
