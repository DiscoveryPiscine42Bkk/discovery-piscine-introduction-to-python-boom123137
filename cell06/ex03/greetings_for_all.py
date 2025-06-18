def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error: argument is not a string")
    else:
        print(f"Welcome, {name}!")
if __name__ == "__main__":
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)