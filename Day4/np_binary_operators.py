marks_list = [10, 20, 30, 40, 50]
marks_dict = {"a":10, "b":20, "c":30, "d":40, "e":50}

marks_list[0] = marks_list[1] + marks_list[2]
print(marks_list)

marks_dict["sum"] = marks_dict["a"] + marks_dict["b"]
print(marks_dict)