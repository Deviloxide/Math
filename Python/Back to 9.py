
def back_to_nine(num):
    big_list = []
    cycles = 0
    cont = True

    while cont:
        total = 0

        num_str = str(num)
        print(num_str)
        num_list = [int(i) for i in num_str]
        print(num_list)

        big_list.append(num_list)

        for i in range(0, len(num_list)):
            total += num_list[i]

        print(total)

        if total == 9 or (total % 9) != 0:
            cont = False
        else:
            num = total

        cycles += 1

    return(big_list, "in {} cycles".format(cycles))

print(back_to_nine((999**999)**99))
