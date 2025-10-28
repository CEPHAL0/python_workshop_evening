# Object Oriented Programming

# Procedural Programming (Function Based)
# Object Oriented Programming (Class and Object Based)

# Concepts of Object Oriented Programming
# Class -> Blueprint of a real life entity with its own attributes and properties and methods
# Object -> Instance of a class with its own values for the properties

# Class Example: Bird, properties: color, weight, native homeland, migration behavior
# Object Example: Danfe, blue, 5, Nepal, north to north
# Pigeon, grey, 3, Asia, South to South


# Class Definition (BluePrint)
class Bird:
    color = ''
    weight = 0
    native_homeland = ''
    migration_behavior = ''

# Object Instantiation
danfe_object = Bird()
danfe_object.color = 'red'
danfe_object.weight = 5
danfe_object.native_homeland = 'Nepal'
danfe_object.migration_behavior = 'North to North'

print(danfe_object.color)

# Object Instantiation
pigeon_object = Bird()
pigeon_object.color = 'grey'
pigeon_object.weight = 3
pigeon_object.native_homeland = 'Asia'
pigeon_object.migration_behavior = 'South to South'

print(pigeon_object.weight)

# Task: Create your own class