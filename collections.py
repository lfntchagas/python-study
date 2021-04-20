
from collections import Counter, defaultdict, namedtuple


mylist = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3]

a = Counter('aaabbccccccdddddddd')
# print(a['a'])
# print(Counter(mylist))


letters = 'aaaaaabbbbcccccdddd'
letter_class = Counter(letters)
#print(letter_class.most_common(1)) # most common letter 

j = list(letter_class)
#print(j)


sentence = "Testing counter and showing how many times does each word show up in this sentence"
# print(Counter(sentence.split()))


d = {'a':10}
#print(d['a'])

e = defaultdict(lambda: 0) # get rid of error in case of key wrong value inputed 

e['correct'] = 100
# print(e['wrong key'])

mytuple = (10,20,30)
print(mytuple[0])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='Sam')

print(sammy[-1])

