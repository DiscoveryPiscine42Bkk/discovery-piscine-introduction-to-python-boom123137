import sys
def shrink(s):
    print(s[:8])
def enlarge(s):
    print(s + 'Z' * (8 - len(s)))
if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:  
            print(arg)
