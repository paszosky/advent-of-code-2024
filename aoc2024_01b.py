file = open('input_day01a.txt', 'r')
# file = open('sample_input.txt', 'r')
input = file.read()
file.close()

left_list = []
right_list = []
score = 0
input_linie = input.split('\n')

for i in input_linie:
    linia = i.split()
    left_list.append(linia[0])
    right_list.append(linia[1])

for i in range(len(left_list)):
    score += int(right_list.count(left_list[i])) * int(left_list[i])

print(score)