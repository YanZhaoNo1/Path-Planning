import random

numbers = [
    [16, 17, 26, 27, 36, 37, 46, 47],
    [56, 57, 66, 67, 76, 77],
    [810, 910, 811, 911, 812, 912]
]
positions = [
    ["左上", "左下", "右上", "右下"],
    ["左上", "左下", "右上", "右下"],
    ["左上", "左下", "右上", "右下"],
    ["左上", "左下"],
    ["左上", "左下", "右上", "右下"]
]
numbers_BCDE = [
    [13, 23, 33, 43, 14, 24, 34, 44, 35, 45],
    [38, 48, 19, 29, 39, 49, 110, 210, 310, 410],
    [53, 73, 54, 64, 74, 55, 75],
    [58, 78, 59, 69, 79, 510, 710]
]

print("\n|>>>>>>>>>>>>第一次<<<<<<<<<<<<\t|>>>>>>>>>>>>第二次<<<<<<<<<<<<\t|>>>>>>>>>>>>第三次<<<<<<<<<<<<\t|\n|\t\t\t\t|\t\t\t\t|\t\t\t\t|")
print("|------------障碍物------------\t|------------障碍物------------\t|------------障碍物------------\t|\n|\t\t\t\t|\t\t\t\t|\t\t\t\t|")
for i in range(3):
    print("|障碍物位置: ", end="")
    for j in range(3):
        random_numbers = random.sample(numbers[j], 1)
        print("%-4d" % random_numbers[0], end="")
    print(end="\t")
print("|\n|\t\t\t\t|\t\t\t\t|\t\t\t\t|")

print("|------------作物区------------\t|------------作物区------------\t|------------作物区------------\t|\n|\t\t\t\t|\t\t\t\t|\t\t\t\t|")
print("|   B   |   C   |   D   |   E\t|   B   |   C   |   D   |   E\t|   B   |   C   |   D   |   E\t|\n|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|")
crops = ["  黄瓜", "  玉米", "  小麦", "  水稻"]
print("|", end="")
for i in range(3):
    random.shuffle(crops)
    print(" |".join(crops), end="\t|")
print("\n|\t\t\t\t|\t\t\t\t|\t\t\t\t|")
for i in range(4):
    print("|", end="")
    for j in range(3):
        random_numbers = random.sample(numbers_BCDE[i], 4)
        print("%c区放置位置: " % chr(i+ord("B")), end="")
        for k in range(4):
            print("%-4d" % random_numbers[k], end="")
        print("", end="\t|")
    print("\n|", end="")
    for j in range(3):
        random_position = random.choice(positions[i])
        print("%c区固定位置: {}".format(random_position) %
              chr(i+ord("B")), end="\t\t|")
    print(end="\n|\t\t\t\t|\t\t\t\t|\t\t\t\t|\n")

crops = ["黄瓜", "西瓜", "玉米"]
print("|------------果实区------------\t|------------果实区------------\t|------------果实区------------\t|\n|\t\t\t\t|\t\t\t\t|\t\t\t\t|")
for i in range(3):
    random_crops = random.sample(crops, 2)
    print("|F区存放果实: {}".format("  ".join(random_crops)), end="\t")
print("|")
for i in range(3):
    random_position = random.choice(positions[4])
    print("|F区固定位置: {}".format(random_position), end="\t\t")
print("|\n")
