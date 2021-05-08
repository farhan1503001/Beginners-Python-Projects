import string
from random import *
#Now creating a string holder variable
value=string.ascii_letters+string.punctuation+string.digits
#Now generating random password
password=''.join(choice(value) for x in range(8,16))

print('\n Generated Password is : '+password)