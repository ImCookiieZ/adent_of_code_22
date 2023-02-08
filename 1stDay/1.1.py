file = open("./input.txt", "r") # Put The numbers here without new line in beginning or end
input_str = file.read()

# variant 1 to calculate
solution1 = 0
for elf in input_str.split("\n\n"):
    elf_calorie = 0
    for item in elf.split("\n"):
        elf_calorie += int(item)
    max_calories = elf_calorie if elf_calorie > max_calories else max_calories
print(solution1)

#variant 2 to calculate
solution2 = max([sum([int(item) for item in elf.split("\n")]) for elf in input_str.split("\n\n")])
print(solution2)