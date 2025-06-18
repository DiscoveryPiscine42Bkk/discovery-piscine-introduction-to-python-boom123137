import sys
params = sys.argv[1:]
filtered_params = [p for p in params if not p.endswith("ism")]
if not filtered_params:
    print("none")
else:
    for p in filtered_params:
        print(p + "ism")