showroom = {'911 turbo', 'wrangler', 'GTR', 'firebird'}
print(len(showroom))
showroom.add('GTR')
# print(showroom)
showroom2 = {'charger', 'dart'}
showroom.update(showroom2)
# print(showroom)
showroom.discard('charger')
showroom.discard('dart')
# print(showroom)


junkyard={'mustang', 'GTR', 'beetle', 'firebird'}

print(showroom.intersection(junkyard))
junkyard.discard('beetle')
print(showroom.union(junkyard))
showroom.union(junkyard)
