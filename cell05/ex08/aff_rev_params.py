import sys
if len(sys.argv) >= 3:
    reversed_params = sys.argv[1:][::-1]
    print(" ".join(reversed_params))
else:
    print("none")