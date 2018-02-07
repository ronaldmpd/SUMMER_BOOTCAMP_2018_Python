
f = open("input.txt", "r")
for line in f.readlines():
    print(line)
f.close()

f1 = open("input1.txt", "r")
print(f1.readline())
f1.close()

print("Todo el archivo input1.txt")
f2 = open("input1.txt", "r")
for line in f2.readlines():
    print(line)
f2.close()