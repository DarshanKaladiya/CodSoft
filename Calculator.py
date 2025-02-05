class Calculator:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
        
    def addition(self):
        total = self.number1 + self.number2
        print(f"Addition of {self.number1} and {self.number2} is = {total}")

    def subtract(self):
        total = self.number1 - self.number2
        print(f"Subtraction of {self.number1} and {self.number2} is = {total}")

    def multi(self):
        total = self.number1 * self.number2
        print(f"Multiplication of {self.number1} and {self.number2} is = {total}")

    def division(self):
        total = self.number1 / self.number2
        print(f"Division of {self.number1} and {self.number2} is = {total}")

def main():
    
    while True:
        print("\n ----- CALCULATOR -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("\nEnter Your Choice ==> "))

        if choice == 1:
            value1 = float(input("Enter Your First Value : "))
            value2 = float(input("Enter Your Second Value : "))
            calc = Calculator(value1,value2)
            calc.addition()
        elif choice == 2:
            value1 = float(input("Enter Your First Value : "))
            value2 = float(input("Enter Your Second Value : "))
            calc = Calculator(value1,value2)
            calc.subtract()
        elif choice  == 3:
            value1 = float(input("Enter Your First Value : "))
            value2 = float(input("Enter Your Second Value : "))
            calc = Calculator(value1,value2)
            calc.multi()
        elif choice == 4:
            value1 = float(input("Enter Your First Value : "))
            value2 = float(input("Enter Your Second Value : "))
            calc = Calculator(value1,value2)
            calc.division()
        elif choice == 5:
            print("Goodbye !")
            break
        else:
            print("Invalid choice ! Please select correct choice.")

if __name__ == "__main__":
    main()