def kaprekar_constant(num, digits):
    kaprekar_list = []
    repeats_list = []
    count = 1
    end = 100

    while count < end:
        if num in repeats_list:
            count = end - 1

        repeats_list.append(num)

        num_str = str(num)
        num_list = [int(i) for i in num_str]
        if len(num_list) < digits:
            while len(num_list) < digits:
                num_list.insert(0, 0)

        descending = sorted(num_list, reverse=True)
        descending_strings = [str(integer) for integer in descending]
        descending_integer = int("".join(descending_strings))

        ascending = sorted(num_list)
        ascending_strings = [str(integer) for integer in ascending]
        ascending_integer = int("".join(ascending_strings))

        resulting_integer = descending_integer - ascending_integer

        resulting_integer_str = str(num) + " (" + str(descending_integer) + ", " + str(ascending_integer) + ")"
        kaprekar_list.append(resulting_integer_str)

        num = resulting_integer

        count += 1

    return kaprekar_list


print(kaprekar_constant(6372, 4))

print(kaprekar_constant(8956, 4))

print(kaprekar_constant(5058, 4))

print(kaprekar_constant(7191, 4))

print(kaprekar_constant(5355, 4))

print(kaprekar_constant(1, 4))

print(kaprekar_constant(6174, 4))

print(kaprekar_constant(9999, 4))

print(kaprekar_constant(617, 3))

print(kaprekar_constant(53955, 5))

print(kaprekar_constant(62964, 5))

print(kaprekar_constant(420876, 5))

num_string = input("Input the starting number:")

num_digits = input("Input the desired number of digits:")

print(kaprekar_constant(num_string, num_digits))
