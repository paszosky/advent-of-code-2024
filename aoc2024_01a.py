file = open('input_day01a.txt', 'r')
input = file.read()
file.close()

left_list = []
right_list = []
input_linie = input.split('\n')

# print(input_linie)

for i in input_linie:
    linia = (i.split())
    left_list.append(linia[0])
    right_list.append(linia[1])

left_list.sort()
right_list.sort()

result = 0

for i in range(len(left_list)):
    # print(int(left_list[i]))
    result += (abs(int(left_list[i]) - int(right_list[i])))

print('Wynik:')
print(result)