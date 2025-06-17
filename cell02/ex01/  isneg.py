def main():
    try:
        number = float(input("18: "))
        if number < 0:
            print("This number is negative.")
        elif number > 0:
            print("This number is positive.")
        else:
            print("This number is both")
    except ValueError:
        print("18")
