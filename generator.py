import os

def generate_base_name(i):
    if i < 10:
        return "day_0"+str(i)
    return "day_"+str(i)

for i in range(1,26):
    name = generate_base_name(i)
    with open("../base.py") as f:
        with open(name+".py", "w") as dest:
            dest.write(f.read())
    with open("test_files/" + name + ".in", "w") as f:
        f.write("\n")
    with open("input_files/" + name + ".in", "w") as f:
        f.write("\n")
