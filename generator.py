# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# cubes_list = create_cubes(10)
# print(cubes_list)

#Instead of create a list and hold it in memory, you yield and just see the last number. It's way more efficient.
def create_cubes(n):
    
    for x in range(n):
        yield x**3
    
# for i in create_cubes(10):
#     print(i)


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a 
        a,b = b,a+b

def simple_gen():
    for x in range(3):
        yield x

# for number in simple_gen():
#     print(number)

g = simple_gen()

# print(next(g))

s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))