def add_one(n):
    n = n + 1
    print(f"Inside add_one, n = {n}")

if __name__ == "__main__":
    x = 5
    print(f"Before add_one, x = {x}")
    add_one(x)
    print(f"After add_one, x = {x}")