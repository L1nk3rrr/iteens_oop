class Example:
    my_str = "Hello"
    _my_protected_str = "Hello"
    __my_private_str = "Hello"

print(Example.my_str)
print(Example._my_protected_str) # Не бажано викликати протектед атрибут чи метод
# print(Example.__my_private_str) #AttributeError


class MyClass:
    def __init__(self) -> None:
        self.public_attribute = "Public attribute"
        self._protected_attribute = "Protected attribute"
        self.__private_attribute = "Private attribute"
    def public_method(self):
        print("This is a public method")
    
    def _protected_method(self):
        print("This is a protected method")
    
    def __private_method(self):
        print("This is a private method")

my_obj = MyClass()
print(my_obj.public_attribute)
print(my_obj.public_method)
print(my_obj._protected_attribute)
print(my_obj._protected_method)
# print(my_obj.__private_attribute) #AttributeError
# print(my_obj.__private_method) #AttributeError


# class ChildClass(ParentClass):
#     # Визначення нових атрибутів та методів підкласу
#     pass

class Vehicle:
    def __init__(self, brand, year) -> None:
        self.brand = brand
        self.year = year
    
    def drive(self):
        print("The vehicle is in motion")
    
    def stop(self):
        print("The vehicle has stopped.")

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.brand} {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, fuel_type) -> None:
        super().__init__(brand, year)
        self.fuel_type = fuel_type
    
    
    def drive(self):
        print("The car is driving on the road")

    def __str__(self) -> str:
        res = super().__str__()
        return f"{res} Fuel type - {self.fuel_type}"

class Bicycle(Vehicle):
    def __init__(self, brand, year, color) -> None:
        super().__init__(brand, year)
        self.color = color
    
    def drive(self):
        print("The bicycle is being pedaled")

    def __str__(self) -> str:
        res = super().__str__()
        return f"{res} Color - {self.color}"

car = Car("Audi", 2023, "diesel")
car.drive() #The car is driving on the road
car.stop() #The vehicle has stopped.
print(car) #Car Audi 2023 Fuel type - diesel
bicycle = Bicycle("Ukraine", 2003, "green")
bicycle.drive() #The bicycle is being pedaled
bicycle.stop() #The vehicle has stopped.
print(bicycle) #Bicycle Ukraine 2003 Color - green




class Author:
    def __init__(self, name) -> None:
        self.name = name
    
    def write(self):
        print(f"{self.name} is writing a book.")

class Book:
    def __init__(self, title: str, author: Author) -> None:
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")


author = Author("John Bob")
book = Book("Python Programming", author)

book.display_info() 
#Title: Python Programming
#Author: John Bob

author.write() #John Bob is writing a book.






class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['extra_attr'] = 100
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.extra_attr)


# Розробіть свої класи з використанням усіх 4 принципів ООП та з 3 типами інкапсуляції(public, private, protected)
# 4 принципи - Поліморфізм, Наслідування, Інкапсуляція, Універсальність (Abstraction)
# Додайте в коді коментарі де ви якраз таки бачите оті принципи, щоб це було зрозуміло для вас та викладача