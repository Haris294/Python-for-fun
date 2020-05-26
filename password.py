
#Random Password Generator

from string import punctuation, ascii_letters, digits
from random import SystemRandom
import random
secure_rand_gen = SystemRandom()
combined = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
pwd = "".join(secure_random.choice(combined) for i in range (10))

print(pwd)
#print([secure_rand_gen.randrange(10) for i in range(10)])
