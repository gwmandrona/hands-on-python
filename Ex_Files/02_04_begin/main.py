NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

#While loop is not as commonly used as a for in loop
i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}") #this one is an f string, which basically makes inputting variables easier

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i} {name}")