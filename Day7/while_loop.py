# if else -> decision do or not do
# for loop -> range/list do or not do
# while -> do until a certain condition is complete

failed = True

# if failed:
#     print("Attempt exam again")
#     marks = input("Enter the newly obtained marks: ")
#     if marks < 40:
#         print("Attemp once more")
#         # marks = ... # continute


while failed:
    marks = int(input("Enter the marks: "))

    if marks < 40:
        print("Failed")
        failed = True
    else:
        print("Passed")
        failed = False


# Eternal loop, press Ctrl + C to stop the execution
while True:
    print("Hello")