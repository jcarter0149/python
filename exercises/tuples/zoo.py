zoo = ('zebra', 'elephant', 'giraffi')

print(zoo.index('elephant'))


def find_animal(animal):
    for i in zoo:
        if i == animal:
            return animal

print(find_animal('elephant'))
print(find_animal('bird'))

(zebra, elephant, giraffi) = zoo
print(zebra)

zoo_b = ["tiger", 'lion', 'monkey']
print('zoo_b', zoo_b)

zoo_list = list(zoo)
print('zoo list', zoo_list)

zoo_list.extend(zoo_b)
print('updated zoo', zoo_list)

updated_zoo = tuple(zoo_list)
print('updated zoo as a tuple', updated_zoo)



