# Constructors
# Special Kind of functions which helps to instantiate an object of the class and set the properties directly
# Constructor Rules:
# Name of the method is same as the name of the class, but in python the name of the method is always __init__
# No return statements


# Constructor creation in the class
class Bird:
    # Constructor Method
    def __init__(self, c, w, mb, nh):
        self.color = c
        self.weight = w
        self.migration_behavior = mb
        self.native_homeland = nh

        # Setting a default property
        self.type = 'Bird'
    
    def print_information(self):
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight}")
        print(f"Migration Behavior: {self.migration_behavior}")
        print(f"Native Homeland: {self.native_homeland}")

pigeon = Bird('gray', 3, 'South to South', 'South Asia')
danfe = Bird('red', 4, 'North to North', 'Nepal')
pigeon.print_information()
danfe.print_information()