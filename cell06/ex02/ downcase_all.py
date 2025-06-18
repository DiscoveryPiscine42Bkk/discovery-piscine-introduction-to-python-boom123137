import sys
def downcase_it(s):
    return s.lower()
if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) == 0:
        print("none")
    else:
        for p in params:
            print(downcase_it(p))