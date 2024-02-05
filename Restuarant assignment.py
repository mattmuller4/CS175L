vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten_free = input('Is anyone in your party gluten free? ')

print('Here are your restuarant choices: ')

if vegetarian == 'Yes' and vegan == 'Yes' and gluten_free == 'Yes':
    print("The Chef's Kitchen")
    print('The Corner Cafe')
elif vegetarian == 'No' and vegan == 'Yes' and gluten_free == 'Yes':
    print('The Corner Cafe')
    print("The Chef's Kitchen")
elif vegetarian == 'No' and vegan == 'No' and gluten_free == 'Yes':
    print('Main Street Pizza Company')
    print('Corner Cafe')
    print("The Chef's Kitchen")
elif vegetarian == 'No' and vegan == 'No' and gluten_free == 'No':
    print("Joe's Gourmet Burgers")
    print('Main Street Pizza Company')
    print('Corner Cafe')
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
elif vegetarian == 'Yes' and vegan == 'No' and gluten_free == 'Yes':
    print('Main Street Pizza Company')
    print('Corner Cafe')
    print("The Chef's Kicthen")
elif vegetarian == 'Yes' and vegan == 'No' and gluten_free == 'No':
    print('Main Street Pizza Company')
    print('Corner Cafe')
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
elif vegetarian == 'Yes' and vegan == 'Yes' and gluten_free == 'No':
    print('Corner Cafe')
    print("The Chef's Kitchen")
elif vegetarian == 'No' and vegan == 'Yes' and gluten_free == 'No':
    print('Corner Cafe')
    print("The Chef's Kitchen")
    
