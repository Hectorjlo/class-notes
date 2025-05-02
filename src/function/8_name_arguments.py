def show_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

show_info(name = "Mateo")

show_info(name = "Andrea", age = 18)