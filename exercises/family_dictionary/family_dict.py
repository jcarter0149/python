my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}
# Krista is my sister and is 42 years old

# single_member = {v + 'is my' + k + 'and is' + v + 'years old' for k in my_family.keys()for v in my_family.values()}

# print(single_member)

print(my_family.values())
print(my_family.keys())
print(my_family.items())


for key in my_family.keys():
    single_member = ('is my ' + key + ' and is')


for values in my_family.values():
    single_member_name = (f'{values["name"]}')
    single_member_age = (f'{str(values["age"])} years old')



print(single_member_name, single_member, single_member_age)

family_stuff = set()
for family_member, member_values in my_family.items():
    family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old')

print(family_stuff)