import random
def random_joke():
    with open ("jokes.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines)
print(random_joke())
import math
print(math.sqrt(256))
print(math.pi)
from datetime import datetime
now = datetime.now()
print(now)