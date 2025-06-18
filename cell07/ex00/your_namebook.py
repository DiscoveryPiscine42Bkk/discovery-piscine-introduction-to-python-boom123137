def array_of_names(names_dict):
    full_names = []
    for first, last in names_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names
if __name__ == "__main__":
    sample_dict = {
        "alice": "smith",
        "bob": "johnson",
        "charlie": "brown"
    }
    result = array_of_names(sample_dict)
    print(result)