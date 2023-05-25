#find lines that have include relative
#get x.md
#copy enchanter to x.md
#replace Enchanter with x.md with the first letter capital

files = []

with open("index.md") as indexfile:
    for line in indexfile:
        if "include_relative" in line:
            loc = line.split("include_relative")[1].split(" ")[1]
            if loc not "enchanter.md":
                files.append(loc)

for f in files:
    print(f)
    uppercase = f.split(".md")[0].capitalize()
    print(uppercase)
