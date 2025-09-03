name_of_item = input("Enter the recipe item: ")

ingredient_1 = input("Enter the first ingredient: ")
ingredient_2 = input("Enter the second ingredient: ")
ingredient_3 = input("Enter the third ingredient: ")

instructions_1 = input("Enter the first step: ")
instructions_2 = input("Enter the second step: ")
instructions_3 = input("Enter the third step: ")

preparation_time = input("Enter the preparation time: ")

print(f"""
Recipe for {name_of_item}:
-----------------
Ingredients Required:
{ingredient_1}
{ingredient_2}
{ingredient_3}
-------------------
Instructions:
1. {instructions_1}
2. {instructions_2}
3. {instructions_3}
------------------
Preparation Time:
{preparation_time}
""")
