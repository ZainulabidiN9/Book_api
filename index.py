
# # Examples of Abstraction and encapsolation 
# # make a class account debit or credit balance in a final account



# # # make a class to Account
# # class Account:
# #     # constructor(To initialize the object)
# #     def __init__(self ,bal , accNo):
# #         self.balance = bal
# #         self.account_no = accNo
# #     #   Debit Function /Method
# #     def debit(self,amount):
# #        self.balance -=amount
# #        print("RS:" , amount , "was debited")
# #        print("Total Baance:",self.get_balance())

# #     # credit function/Method
# #     def credit(self,amount):
# #            self.balance += amount
# #            print("RS:" , amount , "was credited")
# #            print("Total Baance:",self.get_balance())

# #     #  Balance Function 
# #     def get_balance(self):
# #          return self.balance      
               
# #     #  To Create a object /Instance acc1   
# # acc1 = Account(20000 , 11221122)
# # print(acc1.balance )
# # print(acc1.account_no)

# # acc1.debit(1000)
# # acc1.credit(500)
# # acc1.credit(10000)


# # Del function
# # class person:
# #     def hello(self):
# #         print("zain ul abideen")

# # s1 = person()

# # del s1        # del method delete the object 
# # print(s1.hello())


# # inheritance :

# class Car:
#     @staticmethod
#     def start():
#         print("car started ....")

#     @staticmethod
#     def stop():
#         print("Car Ended....")


# class Toyota(Car):
#     def __init__(self , name):
#         self.name = name 


# car1 = Toyota("mrcedes")
        
# print(car1.name)

# print(car1.start())

# print(car1.stop())



# ------------------------------practices in oops--------------------------------


# class Circle:
#     def __init__(self,radius):
#         self.radius = radius


#     def Area(self):
#         return 3.14 * self.radius**2 

#     def Parameter(self):
#             return 2 * 3.14 * self.radius 
     
# c1 = Circle(3.4)
# print(c1.Area())
# print(c1.Parameter())



# class Employee:
#     def __init__(self , role , dept, salary ):
#           self.role = role 
#           self.dept = dept
#           self.salary = salary 

#     def Showdetails(self):
#          print("Role =",self.role)
#          print("department =",self.dept)
#          print("Salary =",self.salary)


# class Engineer(Employee):
#      def __init__(self, name , age):
#         self.name = name
#         self.age =age
#         super().__init__("Supervisor" ,"SC" ,"70,000")


# eng1 = Engineer("zain ul abideen" , 23)
# eng1.Showdetails()

# e1 = Employee("Supervisor" , "CS" , 120000)

# e1.Showdetails()


# class Order:
#     def __init__(self,item,price):
#        self.item = item
#        self.price = price


#     def __gt__(self, order2):
#         return self.price > order2.price


# order1 = Order("chips" , 40)
# order2 = Order("Tea" , 50)

# print(order1 > order2)


# .................Singleton Design Pattern ......................

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance


# obj1 = Singleton()
# obj2 = Singleton()

# print(obj1 is obj2)

# # another Example of singleton design pattern 
# class Logger:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)

#         return cls._instance

#     def log(self,message):
#         print(f"LOG: {message}")

# obj1 = Logger()
# obj2 = Logger()
# obj1.log("Login Successfully")
# obj2.log("Database Connection")
# print(obj1 is obj2)

# ....................Factory Design Pattern ....................

# class CreditCard:
#     def pay(self, amount):
#         print(f"Paid Rs.{amount} using Credit Card")


# class PayPal:
#     def pay(self, amount):
#         print(f"Paid Rs.{amount} using PayPal")


# class PaymentFactory:

#     @staticmethod
#     def create_payment(method):

#         if method == "credit_card":
#             return CreditCard()

#         elif method == "paypal":
#             return PayPal()

#         else:
#             raise ValueError("Invalid payment method")


# payment = PaymentFactory.create_payment("paypal")

# payment.pay(5000)





# def add(*args):
#     return sum(args)

# print(add(12,23,34,54))


# def student_info(**kwargs):
#     print(kwargs)

# student_info(
#     name="Ali",
#     age=20,
#     department="CS"
# )

# students = [
#     {"name": "Ali", "marks": 80},
#     {"name": "Ahmed", "marks": 90},
#     {"name": "Sara", "marks": 70}
# ]

# students.sort(key=lambda student: student["marks"])

# print(students)

# # ----------------comprehensive list --------------------------------

# number = [i*2 for i in range(1,6)]
# print(number)

# # ------------------------inheritence (one class functionality use other class)------------------------------
 
# class EMP:
#     def __init__(self , name , salary):
#          self.name = name 
#          self.salary =  salary 


#     def cal_sal(self):
#         return self.salary

# emp = EMP("zain",50000)
# print(emp.name , emp.salary)
# print(emp.cal_sal())

# # ---------------------------POLYMORPHISM (same interface but different behaviour)--------------------------------

# class Dog:
#     def sound(self):
#         print("BARK")


# class Cat:
#     def sound(self):
#         print("MEOW")

# animals = [Dog() , Cat()]
# for animal in animals:
#     animal.sound()


# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance
# account = BankAccount(50000)

# print(account.get_balance())

# # --------------------Exception handling ----------------------------
# try:
#     age = int(input("Enter age: "))

# except ValueError:
#     print("Invalid age")

# else:
#     print("Age:", age)

# finally:
#     print("Program finished")

# def login_required(func):

#     def wrapper():
#         print("Checking login...")
#         func()

#     return wrapper


# @login_required
# def dashboard():
#     print("Dashboard")


# dashboard()

# ------------------------- Generator (produce value one at a time instead of storing everything in memory)-------------------
# def numbers():
#     for i in range(5):
#         yield i
# for number in numbers():
#     print(number)

# ------------ iteratorc--------------------------------

# num = [1,2,3,345,"zain",67,7]
# iterator = iter(num)
# print(next(iterator))
# print(next(iterator))


# class Employee:

#     def __init__(self, salary):
#         self.salary = salary

#     @property
#     def yearly_salary(self):
#         return self.salary * 12


# employee = Employee(50000)

# print(employee.yearly_salary)





# ------------------------DJANGO INTERVIEW QUESTIONS PRACTICES ---------------------------------------



