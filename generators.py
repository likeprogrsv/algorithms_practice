
def gen_simpl_num():
    
    num = 2
    while True:
        for i in range(1, num + 1):            
            if num != i and num % i == 0 and num / i != num:
                break
            if num // i != 0 and num / i == 1:
                yield num
        num += 1

g = gen_simpl_num()    
print(*(next(g) for i in range(20)))

'''
import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
#random.seed(1)
N = int(input())
# здесь продолжайте программу
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
def gen_pass(N):
    """Password generator"""
    while True:
        password = ''
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            password += chars[indx]        
        yield password

g = gen_pass(N)
print(*(next(g) for i in range(9)), sep='\n')
'''

'''
N = 9

def gen(N):
    a, b, c = 1, 1, 1
    for i in range(1, N + 1):   		
        d = a + b + c
        if i < 4:        	
            # d = 1
            yield 1
        else:
            yield d
            a, b, c = b, c, d

g = gen(N)
print(*(next(g) for i in range(1, N + 1)), end=' ')
'''