import itertools
combos = ["".join(seq) for seq in itertools.product("01", repeat=6)]

combos_valid = []
corners = []
corners_num = 0

print("0" + "\n" + "0" + "\n" + "0" + "\n" + "1" + " 0" + " 0")

for i in range(1, len(combos) + 1):
    if (combos[i-1:i][0][0] == "1" or combos[i-1:i][0][1] == "1" or combos[i-1:i][0][2] == "1" or combos[i-1:i][0][3] == "1") \
            and (combos[i-1:i][0][3] == "1" or combos[i-1:i][0][4] == "1" or combos[i-1:i][0][5] == "1"):
        combos_valid.append(combos[i-1:i])

print(combos_valid)

for i in range(1, len(combos_valid) + 1):
    corners.append(combos_valid[i-1][0][3])
    if combos_valid[i-1][0][3] == "1":
        corners_num += 1

print(corners)

print("{}% of the possible configurations have an eel in the corner.".format((corners_num/len(combos_valid)) * 100))
