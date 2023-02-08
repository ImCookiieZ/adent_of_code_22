file = open("./input.txt", "r") # Put The numbers here without new line in beginning or end
input_str = file.read()

# variant 1 to calculate
all_calories = []
for elf in input_str.split("\n\n"):
    calories = 0
    for item in elf.split("\n"):
        calories += int(item)
    all_calories.append(calories)
maxes = sorted(all_calories, reverse=True)[:3]
solution1 = sum(maxes)
print(solution1)
    

#variant 2 to calculate
solution2 = sum(sorted([sum([int(item) for item in elf.split("\n")]) for elf in input_str.split("\n\n")], reverse=True)[:3])
print(solution2)