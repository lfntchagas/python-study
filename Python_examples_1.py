import time, json
from datetime import datetime
from random import shuffle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import os 
import requests
from random import randint

def return_chromedriver_dir():
    '''Find out directory where 'chromedriver file is and return the dir'''
    for dirpath, dirname, filenames in os.walk(os.getcwd()):
        if 'chromedriver' in filenames:
            return dirpath + '/chromedriver'
        else:
            pass


my_list = [1,2,3, 'Jhon']

mylist = ['one', 'two', 'three']

another_list = ['four', 'five']

new_list = mylist + another_list

popped_item = new_list.pop(0)
new2_list = []
new2_list.append(popped_item)


new3_list = ['a','e','x', 'b', 'c']
num_list = [4,1,8,3,['a', 'b', 'c']]

#print(num_list[4][2])

lst = ['a','b','c']


my_dict = {'key1':'value1', 'key2':'value2'}

prices_lookup = {'apple':2.99, 'oranges':1.99, 'milk': 5.80}

d = {'k1':123, 'k2':[0,1,2], 'k3':{'insidekey':100, 'k4':['a','b','c']}}

#mylist= d['k3']['k4'][2].upper()

t = ('a','a','b',[1,2])

myset = set()
#print(set('parallel'))


arq_file = "/Users/l.chagas/git/python-fromzero/myfile.txt"
arq_file2 = "/Users/l.chagas/git/python-fromzero/my_new_file.txt"

'''
myfile = open("/Users/l.chagas/git/python-fromzero/myfile.txt")
content = myfile.readlines()
#print(type(content))
myfile.close()


with open("/Users/l.chagas/git/python-fromzero/myfile.txt") as my_new_file:
    contents = my_new_file.read()


with open(arq_file2, mode='a') as myfile:
    myfile.write('FOUR ON FOUR\n')


with open(arq_file2, mode='r') as readfile:
    content = readfile.read()
    print(content)

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
'''

color = 'purple'

if color == 'blue':
    print('the color is blue')

elif color =='blue':
    pass

'''
mylist = [1,2,3,4,5,6,7,8,9,10]


for i in mylist:
    if (i % 2) == 0:
        print(f'even number {i}')
    else:
        print(f'odd number {i}')
'''

d = {'k1':1, 'k2': 2, 'k3':3}
'''
x = 0

while x <= 5:
    print(f'the current value of x is {x}')
    x = x + 1
    #x += 1
'''
'''
mystring = 'Sammya'
for letter in mystring:
    if letter =='a':
        break
    print(letter)
'''

user_id = '1=1; UPDATE users SET credits = 1000 WHERE user == 123abd'
#print('SELECT * FROM USERS WHERE USER = ' + user_id)

for num in range(3,11,2):
    #print(num)
    pass

#print(list(range(0,11,2)))

index_count = 0
'''
for letter in 'abcde':
    print('at  index {} the letter is {}'.format(index_count, letter))
    index_count += 1
'''
'''
d = {'mykey':345}
print(345 in d.values())

for i in d.values():
    print(i)
'''
'''
list1 = [0,1,2,3,4]
list2 = [0,1,2,3,4]
list3 = []

for num1 in list1:
    for num2 in list2:
        if num1 != num2:
            print(num1, num2)
            list3.append(num1)
            

print(set(list3))
'''

def add_function(name1, name2):
    return name1 + name2

result = add_function('jose', 'nina')

def say_hello(name='test'):
    print(f'Hello {name}')

def print_result(num1, num2):
    print(num1 + num2) # print doesn't actually return anything to be saved. only prits out the result.

def return_result(num1, num2):
    return num1+ num2 # instead of print out the result, it allows you to save then as a variable.

result = return_result(10,20)



white_space = "\n"

site_list = ['uol.com.br', 'terra.com', 'google.com', 'netvasco.com']

dict_data = {}
count = 0

for item in site_list:
    count = count + 1
    dict_data['Name'] = count
    dict_data['URL'] = item


with open('data.json', 'w') as outfile:
    json.dump(site_list, outfile)


'''
with open('data.json') as json_file:
    data = json.load(json_file)
    print(type(data))
    for i in data:
        print(i)
'''

'''
num_lista = [1,3,5,7,10,12]

def evenfunc(number):
    return number %2 == 0 #return true if result is 0, and false if the result is 1.

def check_even(number):
    even_numbers = []

    for i in number:     
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            pass # don't do anything

    return even_numbers

'''


stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

work_hours = [('Abby', 100), ('Billy', 400), ('Jen', 900), ('Cassie', 800)]
'''
def check_emp_month(emp):
    current_max = 0
    employee_of_month = ''
    for name, hour in emp:
        if hour >= current_max:
            current_max = hour
            employee_of_month = name
        else:
            pass
    return (employee_of_month, current_max)


        
        

        

name, hours = check_emp_month(work_hours)

print(hours)
'''


path = os.getcwd() + '/project-imoves/chromedriver'
#print('getcwd:  ', os.getcwd())
#print('__file__:    ', os.path.dirname(__file__))




#mod_time = os.stat('main.py').st_mtime

#print(os.getcwd())



def return_chromedriver_dir():
    for dirpath, dirname, filenames in os.walk(os.getcwd()):
        #print('Current Path(dirpath):', dirpath)
        #print('Directories:(dirname)', dirname)
        #print('Directories:(filenames)', filenames,'\n')
        if 'chromedriver' in filenames:
            print(dirpath)
            print(filenames)
            return dirpath + '/chromedriver'
        else:
            pass
            #print(dirname)
            #print(filenames)

#chromedriver = return_chromedriver_dir()




def shuffle_list(list):
    shuffle(list)
    return list



mylist_1 = ['', 0, '']

def guess_where(mylist):
    user_guess = [0,1,2]
    user_list = shuffle_list(user_guess)
    shuffle_list(mylist)
    print(f'cups are: {mylist}') 
    user_first_choice = user_list[0] #get user first choice from 1-3 and turn as index position
    print('user choice',user_first_choice) #show user's' choice
    print('user choice in list', mylist[user_first_choice])

    if user_first_choice == mylist[user_first_choice]:
        print('congratulation')
    else:
        pass
    
def myfunc_1(**kwargs):
    # returns 5% of the sum of a and b
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

#myfunc_1(fruit='apple', veggie = 'lettuce')

'''    
def myfunc_2(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['animal']))

myfunc_2(10,20,30, fruit='orange,', food='eggs', animal='dog')
'''

'''functions #10 skyline'''

'''
def myfunc(name):
    a = 0
    e = ''
    for i in name:
        a = a + 1
        if a % 2 ==0:
            c = i.upper()
            e = e + c

        else:
            d = i.lower()
            e = e + d 
    return e
    
a = myfunc('Anthropomorphism')
a = myfunc('ABsTritunIna')
print(a)
'''


'''Warmup section'''

def lesser_of_two_events(a,b):
    if a %2 ==0 and b %2 ==0:
        if a < b:
            return a
        elif True :
            return b

    if (a & 1) ==1 or (b & 1) ==1:
        if a > b:
            return a
        elif True:
            return b



def animal_crackers(text):
    list_text = text.lower().split()
    
    return list_text[0][0] == list_text[1][0]

#animal_crackers('Levelheaded Llama')


def makes_twenty(n1,n2):
    if n1 + n2 == 20 or n1 ==20 or n2 == 20:
        return True

    else:
        return False

'''Level 1 Problems'''


def old_macdonal(name):
    a = name.capitalize()
    s = list(a)
    e = s[3] = s[3].upper()
    s[3] = e
    abcde = "".join(s)
    return abcde

#print(old_macdonal('macdonald'))

def master_yoda(text):
    list_split = text.split()
    list_after_split = []
    for i in list_split[::-1]:
        list_after_split.append(i)

    return " ".join(list_after_split)
    
master = 'We are ready'

def almost_there(n):
    if n >=90 and n <=110 or n >=190 and n <=210:
        return True
    else:
        return False

'''Level 2 Problems'''

def has_33(nums):
    
    for i in range(0,len(nums)-1):
        print(nums[i])
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
        

    '''print(nums)
    for i in nums:     
        a = nums.index(i) # map index position of i to a.
        print('index position of i {} is {}'.format(i, a))
        if i == 3:
            b = a + 1
            print(a)
            print(b)
            if nums[b] == 3:
                return True
            else:
                return False '''
        


            
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result

    '''list_a = []
    for i in text:   
        list_a.append(i*3)
        
    a = "".join(list_a)
    return a'''





def blackjack(*arg):
    sum_arg = sum(arg[0])
    reduct_sum = 0
    if sum_arg <= 21:    
        return sum_arg

    elif sum_arg > 21 and 11 in arg[0]:
        reduct_sum = sum_arg - 11
        if reduct_sum > 21:
            return 'BUST'


def summer_69(*arr):
    array = arr[0]
    save_six = 0
    save_nine = 0

    for i in range(len(array)):
        #print('index position: {0} , array number:{1}'.format(i, array[i]))
        if array[i] == 6:
            save_six = i
        if array[i] == 9:
            save_nine = i + 1

    for i in array[save_six:save_nine]:
        array.remove(i)

    print(array)
    return sum(array)
        

          


'''challenging problems'''
def spy_game(*nums):
    array = nums[0]
    spy_array = []
    
    for i in range(len(array)):
        print('index position: {}, array number {}'.format(i, array[i]))
        if array[i] == 0:
           spy_array.append(array[i])

        elif array[i] ==7:
            spy_array.append((array[i]))

    print(spy_array)

    count_zero = 0
    for i in spy_array:
        
        if i == 0:
            count_zero += 1
            print('number of zeros is:',count_zero)           
            continue          

        elif count_zero == 2 and i == 7:
            print(i)
            return True
        
        else:
            return False

#print(spy_game([0,1,0,7,2,0,4,5,0]))

def spy2_game(nums):
    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1



'''function map'''
'''def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums): # map apply the function (square) to every element in (my_nums)
    print(item)

def splicer(mystring):
    if len(mystring)%2 ==0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer,names)))'''


'''function filter'''
'''def check_even(num):
    return num%2 ==0

mynums = [1,2,3,4,5,6]

list(filter(check_even, mynums))
#or 
for n in filter(check_even,mynums): # filter based off the function condition. Only if it's True.
    print(n)'''

'''lambda expression'''
#lambdas are anonymous function 
square = lambda num: num ** 2
    
mynums = [1,2,3,4,5,6]
#print(list(map(lambda num:num**2, mynums)))

list(filter(lambda num: num%2 ==0, mynums))

#GLOBAL
name = 'This is a Global String'

def greet():
    #ENCLOSING
    #name = 'Sammy'

    def hello():
        #LOCAL
        #name = 'Jen'
        print('Hello ' + name)
    hello()

x = 50
def func():
    global x
    print(f'x is {x}')
    #Global variable is declared so it will affect all the variables
    x = 'NEW VALUE'
    
    print(f'I just Locally changed global x to {x}')


def req():
    res = requests.get('https://www.theoutnet.com')
    if res.status_code == 200:
        return res.status_code
    else:
        return res.status_code
    


def show_current_url(time):
    running_time = time 
    i = 0

    while i < running_time:
        i+=1
        print(i)



def check_win():
    #test for first row
    #print(row3[0][0], row3[1][0], row3[2][0])
    print('printing row3')

    if (row1[0][0] and row2[1][0] and row3[2][0]) or (row3[0][0] and row2[1][0] and row1[2][0]) == 'x' or 'o':
        print('You are the winner diagonal')
        
    elif row1[0][0] and row2[0][0] and row3[0][0] or row1[1][0] and row2[1][0] and row3[1][0] or row1[2][0] and row2[2][0] and row3[2][0] == 'x' or 'o':
        print('You are the winner vertifical')


 


def tic_tac_toe(row1, row2, row3):
    '''show tic tac toe in the screen'''
    print(row1)
    print(row2)
    print(row3)


'''#dictionaries
f_dic = {'t1':[''], 't2':[''], 't3':['']}
s_dic = {'m1':[''], 'm2':[''], 'm3':['']}
t_dic = {'b1':[''], 'b2':[''], 'b3':['']}

#lists
row1 = [f_dic['t1'], f_dic['t2'], f_dic['t3']]
row2 = [s_dic['m1'], s_dic['m2'], s_dic['m3']]
row3 = [t_dic['b1'], t_dic['b2'], t_dic['b3']]

ticlist = ['t1', 't2', 't3', 'm1', 'm2', 'm3', 'b1', 'b2', 'b3']


while True:
        

    question = input('You wish to stop, y for YES or press ENTER to continue \n')
    if question.lower() == 'y':
        break

    else:
                
        for i in range(len(ticlist)):
            
            print(ticlist)
            key = input('Select one item of the list\n') 
            print('key selected', key)
            valor = input(f'Select X or O for {key}\n')

            if key in f_dic:
                f_dic[key][0] = valor
                check_win()
                ticlist.remove(key)
            
            elif key in s_dic:
                s_dic[key][0] = valor
                check_win()
                ticlist.remove(key)
            
            elif key in t_dic:
                t_dic[key][0] = valor
                check_win()
                ticlist.remove(key)


            tic_tac_toe(row1, row2, row3)

            

         

print('Game is over')'''
            


def user_choice():
    

    #Initial
    choice = 'WRONG'
    acceptable_range = range(0,11)
    within_range = False

    #TWO CONDITIONS TO CHECK
    #DIGIT OR WITHIN_RANGE=False

    while choice.isdigit() == False or within_range ==False:

        choice = input("please enter a number (0-10): ")

        #DIGIT CHECK

        if choice.isdigit() == False:
            print("Sorry that is not a digit")

        #RANGE CHECK
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range = False

     

    return int(choice)



game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list:")
    print(game_list)


def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input("pick a position (0,1,2): ")

        if choice not in ['0','1', '2']:
            print("Sorry, Invalid choice! ")
    
    return int(choice)
       
    
def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list


def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? (Y or N)")


        if choice not in ['Y', 'N']:
            print("Sorry, I dont understand, please choose Y or N ")
    
    if choice == "Y":
        return True
    else:
        return False



game_on = True
game_list = [0,1,2]
'''
while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()
'''
   
#Tic tac toe version 2
#player1 = input("Please pick a marker 'X' or 'O' ")
#position = int(input('Please enter a number: '))



def display_board(board): #1
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
        

def player_input(): #2
    player1 = ''
    player2 = ''

    while player1 not in ['X','O']:
        player1 = input('Hi Player1, select between (X or O)\n').upper()
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    
    return (player1, player2)
    
  


def place_marker(board, marker, position): #3
    board[position] = marker



def win_check(board, mark): #4
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark))


def choose_first(): #5
    player1 = '1'
    player2 = '2'
    random_int = str(randint(1,2))
    if random_int == player1:
        return player1
    else:
        return player2


def space_check(board, position): #6-8
    if board[position] == '':
        return True
    else:
        return False


def full_board_check(board): #7
    '''Check if the board is full'''

    for i in board[1:]:
        if i in ['X', 'O']:
            continue
        elif not i:
            return False
    return True

             
def player_choice(board): #8
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position
    

def replay():
    answer =''
    
    while answer not in ['Y', 'N']:
        answer = input("Reply 'Y' If you want to play again otherise 'N'").upper()

        if answer == 'Y':
            return True
        elif answer =='N':

            break


#print('Welcome to Tic Tac Toe!')
'''
while True:
    #Set the game up here
    test_board = ['']*10

    print(test_board)


    player1, player2 = player_input() #2
    display_board(test_board) #1
 
     
    while game_on:
        if full_board_check(test_board):
            print('Game is over')
            break
        

        #Player 1 Turn
        
        print(f'\nPlayer1 - {player1} turn: \n')
        player1_position = player_choice(test_board)#8-6

        if player1_position:
            place_marker(test_board, player1, player1_position)
            display_board(test_board)
            if win_check(test_board,player1):
                print('Player 1 win!!!')
                break
            
  
        
        #Player2's turn.
        print(f'\nPlayer2 - {player2} turn: \n')
        player2_position = player_choice(test_board)

        if player2_position:
            place_marker(test_board, player2, player2_position)
            display_board(test_board)
            if win_check(test_board,player2):
                print('Player 2 win!!!')
                break
    


            
            #pass

    if not replay():
        break'''


mylist3 = [1,2,3]

myset = set()

class Dog():
    
    #ClASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal' # class object attribute



    def __init__(self, breed, name): #Init method will be called automatically when you create an instance of a class. (it is a method)
        
        #Attributes
        #We take in the argument
        # Assign it using self.attribute_name
        self.my_attribute = breed #attributes are characteristics of the object
        self.name = name

        #Expect Boolean True/False
        

    #OPERATIONS/Actions --> Methods
    #Method is a function that is inside of a class that will actually work with the object in some way.
    def bark(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name, number))

#my_dog = Dog(breed='Husky', name='Sammy', spots=False) # instance of a class
my_dog = Dog('Lab', 'Frankie' ) #instance of the object


class Circle():

    #Class object Attribute
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
        self.area = radius*radius*Circle.pi # or self.pi

    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")




class Cachorro(Animal): # driving class - Inheritance

    def __init__(self):
        Animal.__init__(self) # Will inherit the methods from Animal class
        print("dog Created")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am a dog and eating")

    def bark(self):
        print("WOOF!")

    
class Dog1():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Miau!"

niko = Dog1("niko")
felix = Cat("felix")

class Animal1():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Book():

    def __init__(self, title ,author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): #special(magic/Dunder) method for string
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b = Book('Python rocks', 'Jose', 200)

print('-'*200)

