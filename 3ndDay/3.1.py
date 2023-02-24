import string

file = open("./input.txt", "r") # Put The numbers here without new line in beginning or end
input_str = file.read()

# Variant 1
res = 0
for row in input_str.split('\n'):
    cut_index = int(len(row) / 2)
    item1 = row[:cut_index]
    item2 = row[cut_index:]
    double = set(item1).intersection(item2).pop()
    res += string.ascii_letters.find(double) + 1
print(res)

# Variant 2
print(sum([1 + string.ascii_letters.find(set(row[:int(len(row) / 2)]).intersection(row[int(len(row) / 2):]).pop()) for row in input_str.split('\n')]))
