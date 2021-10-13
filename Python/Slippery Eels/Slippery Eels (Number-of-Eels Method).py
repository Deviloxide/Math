import itertools
combos = ["".join(seq) for seq in itertools.product("01", repeat=6)]

combos_valid = []
super_corners = 0
super_total = 0
super_fraction = 0

for i in range(1, len(combos) + 1):
    if (combos[i-1:i][0][0] == "1" or combos[i-1:i][0][1] == "1" or combos[i-1:i][0][2] == "1" or combos[i-1:i][0][3] == "1") \
            and (combos[i-1:i][0][3] == "1" or combos[i-1:i][0][4] == "1" or combos[i-1:i][0][5] == "1"):
        combos_valid.append(combos[i-1:i])

print(combos_valid)

for num in range(1, 7):
    corners = 0
    total = 0
    print("\n" + "For {} eels in a valid configuration".format(num))
    for i in range(1, len(combos_valid) + 1):
        if combos_valid[i-1][0].count("1") == num:
            print(combos_valid[i-1][0])
            total += 1
            if combos_valid[i-1][0][3] == "1":
                corners += 1
    super_corners += corners
    super_total += total
    fraction = corners/total
    super_fraction += fraction
    print("{} corner eels out of {} total".format(corners, total))

print("\n" + "The total probability of getting a corner eel is {}%".format((super_fraction/6) * 100))
