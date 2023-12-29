NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for bananaphone in range(5):
    print(bananaphone)

# enumerate
for i, name in enumerate(NAMES):
        print(f"{i} - {name}")