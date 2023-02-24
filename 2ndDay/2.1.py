file = open("./input.txt", "r") # Put The numbers here without new line in beginning or end
input_str = file.read()

# 1, 1 =  0 -> draw
# 2, 2 =  0 -> draw
# 3, 3 =  0 -> draw
# 1, 2 = -1 -> Second
# 1, 3 = -2 -> First
# 2, 3 = -1 -> Second
# 2, 1 =  1 -> First
# 3, 1 =  2 -> Second
# 3, 2 =  1 -> First

# First 1, -2
# Second -1, 2 

# Variant 1
def check_win(first, second) :
    winner = first - second
    if winner in [1, -2]:
        return 0
    elif winner in [2, -1]:
        return 6
    return 3

res = 0
for row in input_str.split('\n'):
    line = list(row)
    first = ord(line[0]) - ord('A') + 1
    second = ord(line[2]) - ord('X') + 1
    winner = check_win(first, second)
    round = second + winner
    res += round
print(res)

# Variant 2
res = sum([
    (
        (
            0 if (
                (ord(list(row)[0]) - ord('A') + 1) - (ord(list(row)[2]) - ord('X') + 1)
            ) in [1, -2] 
            else 3
        ) * ( 
            2 if (
                (ord(list(row)[0]) - ord('A') + 1) - (ord(list(row)[2]) - ord('X') + 1)
            ) in [-1, 2] 
            else 1
        ) + ord(list(row)[2]) - ord('X') + 1
    ) for row in input_str.split('\n')
])
print(res)

# Unformatted Variant 2
print(sum([((0 if ((ord(list(row)[0]) - ord('A') + 1) - (ord(list(row)[2]) - ord('X') + 1)) in [1, -2] else 3) * (2 if ((ord(list(row)[0]) - ord('A') + 1) - (ord(list(row)[2]) - ord('X') + 1)) in [-1, 2] else 1) + ord(list(row)[2]) - ord('X') + 1) for row in input_str.split('\n')]))
