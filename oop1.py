# це у нас ф-я
def my_func():
    return 1


class MyClass:
    # а ось це вже буде метод класу
    def my_func(cls):
        return 1




class Animal:
    _name = "Animal"
    __description = "Animal description"
    def voice(self):
        print("Я є тварина")
        # дія яка записує в базу даних 
    
    def set_description(self, text):
        if "_animal" in text:
            __description = text


class Cat(Animal):
    def voice(self):
        print("Мяу")
        # виклик батьківського методу
        super(Cat, self).voice()


class Dog(Animal):
    def voice(self):
        print("Гaв")


for class_name in (Cat, Dog):
    object = class_name()
    object.voice()
    print(object._name) # _(назва) це protected атрибут
    # print(object.__description) Так не можна, __(назва) це private атрибут!




# Клас - це шаблон або опис, що визначає властивості і методи, які будуть мати об'єкти певного типу
# Об'єкт - це конкретний екземпляр класу, який має свої унікальні значення властивостей

#Pascal Case - тобто кожна літера слова з великої букви без розділювання (MyPythonClass)
class GoIteens:
    """Це мій клас"""

    attr1 = 42
    attr2 = "Hello world"

    def method1(self, x):
        pass

# print(GoIteens.__dict__) # всі атрибути класу
print(GoIteens.__doc__) # doc string класу
a = 19

class Student:
    def __init__(self, name, age, country="Ukraine"):
        self.name = name
        self.age = age
        self._country = country
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        if "russia" in value.lower():
            raise ValueError("Не приймаємо в університет громадян країни агресора")
        self._country = value
    
    
        

# student1 = Student()
# TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'age'
student1 = Student("Jack", 14)
student2 = Student("Bob", 15, "USA")

print(student1.name, student1.age, student1.country)
print(student2.name, student2.age, student2.country)

student1.country = "USA"
student1.age = 100000
print(student1.name, student1.age, student1.country)






class MyClass:
    def __init__(self, attr1) -> None:
        print("Метод __init__ викликано")
        self.attr1 = attr1
    
    def __new__(cls, *args, **kwargs):
        print(f"Метод __new__ викликано\n{args=}\n{kwargs=}")
        return super().__new__(cls)

    def __del__(self):
        print("Метод __del__ викликано для об'єкта", self.attr1)

    @staticmethod
    def my_static_method():
        print("Це статичний метод")

    def my_non_static_method(self):
        print("А я не статичний метод")

    @classmethod
    def my_class_method(cls):
        print("Це класовий метод")
        print("Це клас: ", cls)
        return cls(10)


MyClass.my_static_method()
# TypeError: MyClass.my_non_static_method() missing 1 required positional argument: 'self'
# MyClass.my_non_static_method()
my_class = MyClass(attr1=2)
my_class.my_non_static_method()
my_class_from_class_method = MyClass.my_class_method()
print(my_class_from_class_method.attr1)

del my_class


# На дз
# Створити батьківський клас, тобто якась абстракція - Тварина, Машина, Персонаж гри, Ноутбук
# загалом будь-що абстрактне
# В цьому класі створити 2 методи, будь-яких
# Також має бути __init__ з декільками атрибутами
# А також створити два дочірніх класи, які будуть мати додаткові атрибути окрім батьківських
# Показати виклики цього всьго, що воно записалось, напрклад за допомогою print(...)

class Animal:
    def __init__(self, name) -> None:
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name)

dog1 = Dog("Bart", "Buldog")
print(dog1.name, dog1.breed)