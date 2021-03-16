def add(n1,n2):
    print(n1 + n2)



# try:
#     # WANT TO ATTEMPT THIS CODE
#     # MAY HAVE AN ERROR
#     result = 10 + 10

# except:
#     print("Hey it looks like you aren't adding correctly")

# else: # execute the block of code if THERE IS NO exception of code.
#     print("Add went well!")
#     print(result)

# try:
#     f = open('testfile', 'w')
#     f.write("write a test line")

# except TypeError: # except occur when there is an error in your try block of code
#     print("There is a Type error")
# except:
#     print('All other exceptions')

# finally: # Finally block always execute no matter what.
#     print('I always run')

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! that is not a number")
            continue

        else:
            print('Yes, thank you', result)
            break

        finally:
            print("End of try/except/finally")
            print("Will run regardless error or not")
            
#problem1
# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print('raised a typeerror msg')


#problem2
# x = 5
# y = 0
# try:
#     z = x/y
# except ZeroDivisionError:
#     print("raised: ZeroDivisionError")
# finally:
#     print("All done")


#problem3
def ask():

    while True:
        try:
            number = int(input('Input an integer'))
        except:
            print("An error occured! Please try again!\n")
            continue
        else:
            print('thank you, your number squared is: ', number ** 2)
            break

ask()

# pylint myexample.py -r y
