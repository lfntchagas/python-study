import argparse

class Dog():
    # SELF keyword connect the object to the class
    # CLASS OBJECT ATTRIBUTE
    species = 'mammal'
    
    def __init__(self,breed, name): # attributes of a class. they are the characteristics of the object.
        self.breed = breed
        self.name = name

    def bark(self, number): # Method
        print('Wolf! My name is  {} and my number is {}'.format(self.name, number))



my_dog = Dog(breed='husky', name='Frankie')


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")




class Cat(Animal): # DERIVE CLASS

    def __init__(self):
        Animal.__init__(self)
        print("Cat Created")

    def eat(self):
        print("My cat is eating")

    def bark(self):
        print("WOOF!")



#dolly_cat = Cat()



class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi # either Circle.pi or self.pi. that only works for class object attribute

    def get_circumference(self):
        return self.radius * self.pi * 2



class Book():

    def __init__(self, author, pages, title):

        self.author = author
        self.pages = pages
        self.title = title

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

      


harry_potter = Book(author='J.K Howling', pages=500 , title='Philosopher stone')


class Account():

    def __init__(self, owner, balance=0 ):
        self.owner = owner
        self.balance = balance


    def deposit(self, value):
        self.balance = self.balance + value
        print(f'Deposit of {value} has been Accepted')

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            print("Withdrawl accepted")
        else:
            print("Sorry not enough funds!")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

       
acct1 = Account('Jose',100)

acct1.deposit(50)
acct1.withdraw(100)










