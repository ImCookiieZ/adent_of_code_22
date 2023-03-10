file = open("./input.txt", "r") # Put The numbers here without new line in beginning or end
input_str = file.read()
# -1 loose 
#  0 draw 
#  1 win
# number = Letter - 'Y'
# [a,b,c][number % 3]

# Variant 1

def my_choice(enemy, result):
    possible = [1, 2, 3]  # 1 = Rock, 2 = Paper, 3 = Scissors
    my_answer = possible[(enemy  + result) % 3]
    return my_answer
    
res = 0
for row in input_str.split('\n'):
    line = list(row)
    first = ord(line[0]) - ord('A')
    second = ord(line[2]) - ord('Y')  # make it -1, 0, 1
    answer = my_choice(first, second)

    second_points = [3, 6, 0]
    round = answer + second_points[second]
    res += round
print(res)

# Variant 2

print(sum([
        [3, 6, 0][ord(list(row)[2]) - ord('Y')]  # points for draw etc
        + [1, 2, 3][(ord(list(row)[0]) - ord('A') + ord(list(row)[2]) - ord('Y')) % 3]  # points fom own choose
        for row in input_str.split('\n')
    ]))

# Variant 2 in one line

print(sum([[3, 6, 0][ord(list(row)[2]) - ord('Y')] + [1, 2, 3][(ord(list(row)[0]) - ord('A') + ord(list(row)[2]) - ord('Y')) % 3] for row in input_str.split('\n')]))