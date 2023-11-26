all_data = [
    ['John', 'Emily', 'Michael', 'Mary', 'Steven'], 
    ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']
    ]

#find all names with more than one a

names_of_interest = []

for names in all_data:
    enough_as = [name for name in names if name.count('a')>=2]
    names_of_interest.extend(enough_as)

print(names_of_interest)