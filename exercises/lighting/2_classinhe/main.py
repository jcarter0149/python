from dog import Dog
from pet import Pet

corgi = Dog("corgi")

Winston = Pet("Winston", corgi)

Winston.set_owner("Jake")

print(Winston)