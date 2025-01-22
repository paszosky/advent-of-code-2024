file = open('input_day02.txt', 'r')
input = file.read()
file.close()

line = input.split('\n')
print(line)

isSafe = 0

for i in line:
    level = i.split()
    dlugosc = len(level)
    print('Linia: ')
    # print(dlugosc)
    print(level)

    if int(level[0]) > int(level[1]):
        # print('malejace')
        for d in range(dlugosc):
            # print(d)
            if d == (dlugosc - 1):
                print('SAFE')
                isSafe += 1
                break
            else:
                if int(level[d]) > int(level[d+1]):
                    # print('Malejący')
                    if int(level[d]) - int(level[d+1]) <= 3:
                        print('Malejący ok')
                    else:
                        print('Unsafe')
                        break
                else:
                    print('Unsafe')
                    break

    elif  int(level[0]) < int(level[1]):
        # print('rosnace')
        for d in range(dlugosc):
            # print(d)
            if d == (dlugosc - 1):
                print('SAFE')
                isSafe += 1
                break
            else:
                if int(level[d]) < int(level[d+1]):
                    # print('Rosnący')
                    if int(level[d+1]) - int(level[d])<= 3:
                        print('Rosnący ok')
                    else:
                        print('Unsafe')
                        break
                else:
                    print('Unsafe')
                    break
    else:
        print('unsafe')

print('There is ' + str(isSafe) + ' safe reports!')